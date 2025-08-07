# gspo_powl_generation_openai_reward_fixed.py
# --------------------------------------------------------------
#  Adapted from the original GRPO script to use GSPO (sequence‑
#  level importance sampling) as introduced in: Group Sequence
#  Policy Optimization, 2025.
# --------------------------------------------------------------

import os
import json
import random
import re
import requests
from typing import List

import torch
import pm4py
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import GRPOConfig, GRPOTrainer          # GSPO via config
from pm4py.objects.powl.obj import (
    StrictPartialOrder,
    OperatorPOWL,
    Transition,
    SilentTransition,
)
from pm4py.objects.process_tree.obj import Operator

# ---------------------------------------------------------------------------#
# 1. Configuration & Hyperparameters                                          #
# ---------------------------------------------------------------------------#
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

# --- Directory and Model Configuration ---
TRAIN_DATA_DIR = "training"
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B"
OUTPUT_DIR = "gspo_qwen_powl_generator_openai_reward"  # renamed

# --- Training Hyperparameters (GSPO paper defaults) ---
MAX_PROMPT_TOKENS = 4096
MAX_COMPLETION_TOKENS = 4096
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 5e-6
KL_BETA = 0.04           # β used in GSPO examples
EPSILON = 3e-4           # two‑sided clipping ε
MAX_TRAINING_STEPS = 1000
NUM_GENERATIONS = 4
MAX_DATASET_SAMPLES = 500

# --- Logging and Saving Configuration ---
LOGGING_STEPS = 1
SAVE_STEPS = 100

# --- OpenAI API Configuration ---
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-4.1-mini"

# ---------------------------------------------------------------------------#
# 2. Prompt and Data Loading                                                  #
# ---------------------------------------------------------------------------#

def get_powl_prompt(description: str, activities: List[str]) -> str:
    activities_str = ", ".join(f"'{a}'" for a in activities)
    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) is a partially ordered graph representation ...
[unchanged doc‑string omitted for brevity]
DESCRIPTION: {description}
ACTIVITIES (use these exactly, same names): [{activities_str}]

Respond with valid Python code only, defining 'root'.
"""

def load_limited_dataset(data_dir: str, max_samples: int) -> Dataset:
    desc_folder = os.path.join(data_dir, "textual_descriptions")
    powl_folder = os.path.join(data_dir, "powl")
    if not (os.path.exists(desc_folder) and os.path.exists(powl_folder)):
        raise FileNotFoundError(f"Data directories not found in '{data_dir}'.")
    file_names = [f for f in os.listdir(desc_folder) if f.endswith(".json")]
    random.shuffle(file_names)
    data = []
    for fn in file_names[:max_samples]:
        stem = os.path.splitext(fn)[0]
        with open(os.path.join(desc_folder, fn), encoding="utf-8") as f:
            desc = json.load(f)
        py_path = os.path.join(powl_folder, f"{stem}.py")
        if not os.path.exists(py_path):
            continue
        with open(py_path, encoding="utf-8") as f:
            powl_code = f.read()
        prompt = get_powl_prompt(desc["description"], desc["activities"])
        data.append({"prompt": prompt, "reference_completion": powl_code})
    print(f"Loaded {len(data)} samples.")
    return Dataset.from_list(data)

dataset = load_limited_dataset(TRAIN_DATA_DIR, MAX_DATASET_SAMPLES)

# ---------------------------------------------------------------------------#
# 3. Reward Function (OpenAI grader)                                          #
# ---------------------------------------------------------------------------#
def get_openai_grading_prompt(original_prompt: str, completions: List[str]) -> str:
    intro = f"""
You are an expert in process modeling. Evaluate the following Python snippets produced for this prompt:
---
{original_prompt}
---
Return a JSON: {{"grades": [float,...]}} with each grade in [-1.0, 1.0].
"""
    body = "\n".join(
        f"\n--- RESPONSE {i+1} ---\n```python\n{c}\n```"
        for i, c in enumerate(completions)
    )
    outro = f"\nNumber of grades **must** equal {len(completions)}."
    return intro + body + outro

def openai_grading_reward_function(completions: List[str], **kwargs) -> List[float]:
    BAD = -1.0
    prompt = kwargs.get("prompts", [""])[0]
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY env var missing.")
        return [BAD] * len(completions)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "user", "content": get_openai_grading_prompt(prompt, completions)}],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
    }

    try:
        r = requests.post(OPENAI_API_URL, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        grades = json.loads(
            r.json()["choices"][0]["message"]["content"]
        ).get("grades", [])
        print(f"--- GRADES THIS STEP: {grades} ---")
        return [float(g) for g in grades]
    except Exception as e:
        print(f"Grading failed: {e}")
        return [BAD] * len(completions)

# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer & GSPO Trainer                                          #
# ---------------------------------------------------------------------------#
model_load_path = MODEL_NAME
resume_from = None
if os.path.isdir(OUTPUT_DIR):
    ckpts = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if ckpts:
        latest = max(ckpts, key=lambda d: int(re.search(r"-(\d+)$", d).group(1)))
        model_load_path = os.path.join(OUTPUT_DIR, latest)
        resume_from = model_load_path
        print(f"▶️ Resuming from {model_load_path}")
    else:
        print(f"🆕 No checkpoint found, starting fresh.")
else:
    print(f"🆕 Output dir {OUTPUT_DIR} does not exist yet; starting fresh.")

tokenizer = AutoTokenizer.from_pretrained(model_load_path, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    model_load_path, torch_dtype=torch.bfloat16, device_map="auto"
)

# --- GSPO‑specific config --------------------------------------------------#
training_args = GRPOConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=PER_DEVICE_BATCH,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    learning_rate=LEARNING_RATE,
    beta=KL_BETA,
    epsilon=EPSILON,                       # sequence‑level clipping
    importance_sampling_level="sequence",  # ★ GSPO switch
    loss_type="grpo",                      # recommended in docs
    max_steps=MAX_TRAINING_STEPS,
    max_prompt_length=MAX_PROMPT_TOKENS,
    max_completion_length=MAX_COMPLETION_TOKENS,
    num_generations=NUM_GENERATIONS,
    remove_unused_columns=False,
    bf16=True,
    logging_steps=LOGGING_STEPS,
    save_steps=SAVE_STEPS,
    report_to="none",
)

trainer = GRPOTrainer(           # GSPO via config flags
    model=model,
    args=training_args,
    train_dataset=dataset,
    reward_funcs=[openai_grading_reward_function],
)

# ---------------------------------------------------------------------------#
# 5. Training Execution                                                       #
# ---------------------------------------------------------------------------#
print("\n--- Starting GSPO Training (sequence‑level) ---")
print(f"Logging every {LOGGING_STEPS} steps | checkpoints every {SAVE_STEPS} steps.\n")
trainer.train(resume_from_checkpoint=resume_from)

print("\n✔️ Training complete.")
trainer.save_model(OUTPUT_DIR)
print(f"Model & tokenizer saved to {OUTPUT_DIR}")
