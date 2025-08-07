# ppo_powl_generation_openai_reward.py
#
# Fine‑tunes a causal‑LM with PPO, using an OpenAI‑based grading
# function as the scalar reward signal.  The model learns to
# generate Python code that builds a POWL process model (“root”)
# from a natural‑language description.

import os
import json
import random
import time
import re
import requests
from typing import List, Dict

import torch
from datasets import Dataset
from transformers import AutoTokenizer
from trl import (
    PPOConfig,
    PPOTrainer,
    AutoModelForCausalLMWithValueHead,  # adds a value‑head required by PPO
    create_reference_model,            # lighter ref‑model sharing weights
)

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator


# ---------------------------------------------------------------------------#
# 1. Configuration & Hyper‑parameters                                         #
# ---------------------------------------------------------------------------#
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

# --- Directories & models --------------------------------------------------#
TRAIN_DATA_DIR = "training"
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B"
OUTPUT_DIR = "ppo_qwen_powl_generator_openai_reward"

# --- RL‑specific hyper‑parameters -----------------------------------------#
MAX_PROMPT_TOKENS      = 4096
MAX_COMPLETION_TOKENS  = 4096
BATCH_SIZE             = 1            # PPOConfig.batch_size
MINI_BATCH_SIZE        = 1            # PPOConfig.mini_batch_size
GRAD_ACC_STEPS         = 4            # PPOConfig.gradient_accumulation_steps
LEARNING_RATE          = 5e-6
INIT_KL_COEF           = 0.1          # PPOConfig.init_kl_coef
TOTAL_PPO_STEPS        = 1000
MAX_DATASET_SAMPLES    = 500

# --- Logging & checkpointing ----------------------------------------------#
LOG_EVERY_STEPS        = 1
SAVE_EVERY_STEPS       = 100

# --- OpenAI API for reward -------------------------------------------------#
OPENAI_API_URL   = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL     = "gpt-4.1-mini"
OPENAI_TIMEOUT   = 60


# ---------------------------------------------------------------------------#
# 2. Prompt engineering & dataset loading                                    #
# ---------------------------------------------------------------------------#
def get_powl_prompt(description: str, activities: List[str]) -> str:
    """Compose the few‑shot prompt that asks the policy to emit Python code."""
    activities_str = ", ".join(f"'{a}'" for a in activities)
    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) …  —— *prompt trimmed for brevity* —— …

DESCRIPTION: {description}
ACTIVITIES (use these exactly, same names): [{activities_str}]

Respond with valid Python code only, defining 'root'.
"""


def load_limited_dataset(data_dir: str, max_samples: int) -> Dataset:
    """Return an HF Dataset with one column called `text` (expected by PPOTrainer)."""
    desc_dir = os.path.join(data_dir, "textual_descriptions")
    powl_dir = os.path.join(data_dir, "powl")
    if not (os.path.isdir(desc_dir) and os.path.isdir(powl_dir)):
        raise FileNotFoundError(f"'{data_dir}' does not contain required sub‑folders.")

    files = [f for f in os.listdir(desc_dir) if f.endswith(".json")]
    random.shuffle(files)
    records: List[Dict[str, str]] = []

    for name in files[:max_samples]:
        base = os.path.splitext(name)[0]
        with open(os.path.join(desc_dir, name), encoding="utf-8") as fd:
            desc = json.load(fd)
        if not os.path.isfile(os.path.join(powl_dir, f"{base}.py")):
            continue  # skip examples that have no reference code
        prompt = get_powl_prompt(desc["description"], desc["activities"])
        records.append({"text": prompt})

    print(f"Loaded {len(records)} prompts.")
    return Dataset.from_list(records)


dataset = load_limited_dataset(TRAIN_DATA_DIR, MAX_DATASET_SAMPLES)
# Shuffle once so every run sees a different ordering (seeded above).
dataset = dataset.shuffle(seed=SEED)


# ---------------------------------------------------------------------------#
# 3. Reward function (unchanged)                                             #
# ---------------------------------------------------------------------------#
def _openai_grade_batch(original_prompt: str, completions: List[str]) -> List[float]:
    """Call OpenAI once to grade N completions for the same prompt."""
    BAD = -1.0
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌  OPENAI_API_KEY not set; all rewards = -1.0")
        return [BAD] * len(completions)

    # Compose system/user message
    def _grading_prompt() -> str:
        intro = f"""
You are an expert in process modelling. Evaluate the following Python snippets …
Prompt:
---
{original_prompt}
---

Grade each response between -1.0 and 1.0. Return JSON: {{ "grades": [...] }}
"""
        body = "\n".join(
            f"\n--- RESPONSE {i+1} ---\n```python\n{code}\n```"
            for i, code in enumerate(completions)
        )
        return intro + body

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "user", "content": _grading_prompt()}],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
    }

    try:
        resp = requests.post(
            OPENAI_API_URL, headers=headers, json=payload, timeout=OPENAI_TIMEOUT
        )
        resp.raise_for_status()
        grades_json = json.loads(
            resp.json()["choices"][0]["message"]["content"].strip()
        )
        grades = grades_json.get("grades", [])
        if len(grades) != len(completions):
            raise ValueError("Grade list length mismatch.")
        print(f"✅  Grades: {grades}")
        return [float(g) for g in grades]
    except Exception as exc:
        print(f"❌  OpenAI grading failed: {exc}")
        return [BAD] * len(completions)


def reward_fn(prompt: str, completion: str) -> float:
    """Helper that returns a scalar reward for a single query/response pair."""
    return _openai_grade_batch(prompt, [completion])[0]


# ---------------------------------------------------------------------------#
# 4. Tokenizer, model & PPO‑trainer setup                                    #
# ---------------------------------------------------------------------------#
# If we trained before, resume from the most recent checkpoint.
model_load_path = MODEL_NAME
resume_ckpt = None
if os.path.isdir(OUTPUT_DIR):
    ckpts = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if ckpts:
        ckpts.sort(key=lambda n: int(re.search(r"checkpoint-(\d+)", n).group(1)))
        resume_ckpt = os.path.join(OUTPUT_DIR, ckpts[-1])
        model_load_path = resume_ckpt
        print(f"🔄  Resuming from {resume_ckpt}")
    else:
        print(f"🚀  No checkpoint found; starting from base model.")

# Tokenizer
print("🔧  Loading tokenizer …")
tokenizer = AutoTokenizer.from_pretrained(model_load_path, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

# Policy and reference models (with value head)
print("🔧  Loading policy model …")
policy = AutoModelForCausalLMWithValueHead.from_pretrained(
    model_load_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

print("🔧  Building frozen reference model …")
ref_policy = create_reference_model(policy)  # shares weights where possible

# PPO configuration --------------------------------------------------------#
ppo_cfg = PPOConfig(
    batch_size=BATCH_SIZE,
    mini_batch_size=MINI_BATCH_SIZE,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    learning_rate=LEARNING_RATE,
    init_kl_coef=INIT_KL_COEF,
    steps=TOTAL_PPO_STEPS,
    seed=SEED,
    log_with=None,               # stdout logging only
)

ppo_trainer = PPOTrainer(
    config=ppo_cfg,
    model=policy,
    ref_model=ref_policy,
    tokenizer=tokenizer,
)

# ---------------------------------------------------------------------------#
# 5. Training loop                                                           #
# ---------------------------------------------------------------------------#
print("\n=== PPO training starts ============================================")
generation_kwargs = {
    "max_new_tokens": MAX_COMPLETION_TOKENS,
    "do_sample": True,
    "top_k": 0,
    "top_p": 1.0,
    "pad_token_id": tokenizer.eos_token_id,
}

start_time = time.time()
save_counter = 0

for step in range(1, TOTAL_PPO_STEPS + 1):
    # 1. Sample one prompt (or a small batch) ------------------------------#
    sample = dataset[random.randrange(len(dataset))]
    prompt_text = sample["text"]

    query_tensor = tokenizer(
        prompt_text,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_PROMPT_TOKENS,
    )["input_ids"].to(policy.pretrained_model.device)

    # 2. Generate a completion --------------------------------------------#
    response_tensor = ppo_trainer.generate(
        [query_tensor.squeeze(0)],              # PPOTrainer expects a list
        return_prompt=False,
        **generation_kwargs,
    )[0]
    completion_text = tokenizer.decode(response_tensor, skip_special_tokens=True)

    # 3. Compute scalar reward --------------------------------------------#
    rew = reward_fn(prompt_text, completion_text)
    reward_tensor = torch.tensor(rew, device=policy.pretrained_model.device)

    # 4. Optimise the policy ----------------------------------------------#
    stats = ppo_trainer.step(
        [query_tensor.squeeze(0)], [response_tensor], [reward_tensor]
    )

    # 5. Logging -----------------------------------------------------------#
    if step % LOG_EVERY_STEPS == 0:
        rewards_log = stats.get("ppo/returns/mean", rew)
        kl_log = stats.get("trainer/kl", float("nan"))
        print(f"[{step:04d}/{TOTAL_PPO_STEPS}] reward={rewards_log:.3f}  kl={kl_log:.3f}")

    # 6. Periodic checkpoint ----------------------------------------------#
    if step % SAVE_EVERY_STEPS == 0:
        ckpt_dir = os.path.join(OUTPUT_DIR, f"checkpoint-{step}")
        os.makedirs(ckpt_dir, exist_ok=True)
        policy.save_pretrained(ckpt_dir)
        tokenizer.save_pretrained(ckpt_dir)
        save_counter += 1
        print(f"💾  Saved checkpoint to {ckpt_dir}")

elapsed = time.time() - start_time
print(f"✅  Training finished in {elapsed/60:.1f} min with {save_counter} checkpoints.")

# ---------------------------------------------------------------------------#
# 6. Final model export                                                     #
# ---------------------------------------------------------------------------#
print("🔒  Saving final policy and tokenizer …")
policy.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"🎉  Final artefacts written to {OUTPUT_DIR}")
