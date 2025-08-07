# ppo_powl_generation_openai_reward.py
#
# RLHF fine‑tuning with PPO + OpenAI grader reward.
# Automatically adapts to the version of `trl` that is installed
# (0.7 → 0.21 tested).

import os
import re
import json
import time
import random
import inspect
import requests
from typing import List, Dict

import torch
from datasets import Dataset
from transformers import AutoTokenizer
from trl import (
    PPOConfig,
    PPOTrainer,
    AutoModelForCausalLMWithValueHead,
    create_reference_model,
)

# ---------------------------------------------------------------------------#
# 1.  Configuration                                                           #
# ---------------------------------------------------------------------------#
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

TRAIN_DATA_DIR   = "training"
MODEL_NAME       = "Qwen/Qwen2.5-Coder-3B"
OUTPUT_DIR       = "ppo_qwen_powl_generator_openai_reward"

MAX_PROMPT_TOKENS     = 4096
MAX_COMPLETION_TOKENS = 4096
BATCH_SIZE            = 1
MINI_BATCH_SIZE       = 1
GRAD_ACC_STEPS        = 4
LEARNING_RATE         = 5e-6
INIT_KL_BETA          = 0.1           # we’ll inject this under the right name
TOTAL_PPO_STEPS       = 1000
MAX_DATASET_SAMPLES   = 500

LOG_EVERY_STEPS  = 1
SAVE_EVERY_STEPS = 100

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL   = "gpt-4.1-mini"
OPENAI_TIMEOUT = 60

# ---------------------------------------------------------------------------#
# 2.  Prompt helper & data loading                                           #
# ---------------------------------------------------------------------------#
def get_powl_prompt(description: str, activities: List[str]) -> str:
    acts = ", ".join(f"'{a}'" for a in activities)
    return f"""Generate a POWL model … (prompt trimmed) …

DESCRIPTION: {description}
ACTIVITIES (use these exactly, same names): [{acts}]

Respond with valid Python code only, defining 'root'.
"""

def load_limited_dataset(root: str, max_samples: int) -> Dataset:
    desc_dir = os.path.join(root, "textual_descriptions")
    code_dir = os.path.join(root, "powl")
    files = [f for f in os.listdir(desc_dir) if f.endswith(".json")]
    random.shuffle(files)
    rows: List[Dict[str, str]] = []
    for name in files[:max_samples]:
        base = os.path.splitext(name)[0]
        with open(os.path.join(desc_dir, name), encoding="utf-8") as fd:
            d = json.load(fd)
        if not os.path.isfile(os.path.join(code_dir, f"{base}.py")):
            continue
        rows.append({"query": get_powl_prompt(d["description"], d["activities"])})
    print(f"Loaded {len(rows)} prompts.")
    return Dataset.from_list(rows).shuffle(seed=SEED)

dataset = load_limited_dataset(TRAIN_DATA_DIR, MAX_DATASET_SAMPLES)

# ---------------------------------------------------------------------------#
# 3.  OpenAI grading reward                                                  #
# ---------------------------------------------------------------------------#
def _grade(original_prompt: str, completions: List[str]) -> List[float]:
    BAD = -1.0
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("❌ OPENAI_API_KEY not set; rewards default to -1.0")
        return [BAD] * len(completions)

    intro = f"""
You are an expert in process modelling. Evaluate the Python snippets below …
Prompt:
---
{original_prompt}
---
Return JSON {{ "grades": [...] }} with a float in [-1.0,1.0] for each snippet.
"""
    body = "\n".join(
        f"\n--- RESPONSE {i+1} ---\n```python\n{c}\n```" for i, c in enumerate(completions)
    )
    payload = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "user", "content": intro + body}],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
    }
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    try:
        r = requests.post(OPENAI_API_URL, json=payload, headers=headers, timeout=OPENAI_TIMEOUT)
        r.raise_for_status()
        grades = json.loads(r.json()["choices"][0]["message"]["content"])["grades"]
        print(f"✅ grades: {grades}")
        return [float(g) for g in grades]
    except Exception as exc:
        print(f"❌ grading failed: {exc}")
        return [BAD] * len(completions)

def reward_fn(prompt: str, completion: str) -> float:
    return _grade(prompt, [completion])[0]

# ---------------------------------------------------------------------------#
# 4.  Model & trainer                                                        #
# ---------------------------------------------------------------------------#
# auto‑resume
resume_ckpt = None
if os.path.isdir(OUTPUT_DIR):
    ckpts = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if ckpts:
        ckpts.sort(key=lambda n: int(re.search(r"checkpoint-(\d+)", n).group(1)))
        resume_ckpt = os.path.join(OUTPUT_DIR, ckpts[-1])
        print(f"🔄 Resuming from {resume_ckpt}")

model_path = resume_ckpt if resume_ckpt else MODEL_NAME

tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

policy = AutoModelForCausalLMWithValueHead.from_pretrained(
    model_path, torch_dtype=torch.bfloat16, device_map="auto"
)
ref_model = create_reference_model(policy)

# ---- Build PPOConfig with version‑aware kwargs ---------------------------#
cfg_kwargs = dict(
    batch_size=BATCH_SIZE,
    mini_batch_size=MINI_BATCH_SIZE,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    learning_rate=LEARNING_RATE,
    seed=SEED,
    log_with=None,
)
sig = inspect.signature(PPOConfig)
if "init_kl_coef" in sig.parameters:
    cfg_kwargs["init_kl_coef"] = INIT_KL_BETA
elif "init_kl_coeff" in sig.parameters:
    cfg_kwargs["init_kl_coeff"] = INIT_KL_BETA
elif "kl_penalty_beta" in sig.parameters:
    cfg_kwargs["kl_penalty_beta"] = INIT_KL_BETA

ppo_cfg = PPOConfig(**cfg_kwargs)
ppo_trainer = PPOTrainer(config=ppo_cfg, model=policy, ref_model=ref_model, tokenizer=tokenizer)

# ---------------------------------------------------------------------------#
# 5.  Training loop                                                          #
# ---------------------------------------------------------------------------#
gen_args = dict(
    max_new_tokens=MAX_COMPLETION_TOKENS,
    do_sample=True,
    top_k=0,
    top_p=1.0,
    pad_token_id=tokenizer.eos_token_id,
)

print("\n=== PPO training ==================================================")
start = time.time()
for step in range(1, TOTAL_PPO_STEPS + 1):
    sample = dataset[random.randrange(len(dataset))]
    q = sample["query"]
    q_ids = tokenizer(q, return_tensors="pt", truncation=True,
                      max_length=MAX_PROMPT_TOKENS)["input_ids"].to(policy.device)

    # rollout
    r_ids = ppo_trainer.generate([q_ids.squeeze(0)], return_prompt=False, **gen_args)[0]
    completion = tokenizer.decode(r_ids, skip_special_tokens=True)

    # scalar reward
    reward = torch.tensor(reward_fn(q, completion), device=policy.device)

    # optimisation
    stats = ppo_trainer.step([q_ids.squeeze(0)], [r_ids], [reward])

    if step % LOG_EVERY_STEPS == 0:
        print(f"[{step:04d}/{TOTAL_PPO_STEPS}] reward={reward.item():+.3f} "
              f" kl={stats.get('trainer/kl', float('nan')):.3f}")

    if step % SAVE_EVERY_STEPS == 0:
        ckpt_dir = os.path.join(OUTPUT_DIR, f"checkpoint-{step}")
        os.makedirs(ckpt_dir, exist_ok=True)
        policy.save_pretrained(ckpt_dir)
        tokenizer.save_pretrained(ckpt_dir)
        print(f"💾 checkpoint saved → {ckpt_dir}")

print(f"✅ finished in {(time.time()-start)/60:.1f} min")

policy.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"🎉 final model saved to {OUTPUT_DIR}")
