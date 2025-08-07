#!/usr/bin/env python
# ppo_powl_generation_openai_reward.py
# Compatible with: transformers ≥ 4.42, trl ≥ 0.22.0  ✅

import os
import re
import json
import random
from typing import List, Dict

import torch
import numpy as np
import requests
import pm4py
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from trl import (
    AutoModelForCausalLMWithValueHead,
    PPOConfig,
    PPOTrainer,
)
from transformers import SequenceClassifierOutput
from trl.core import LengthSampler
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# ---------------------------------------------------------------------------#
# 1. Configuration & Hyperparameters                                          #
# ---------------------------------------------------------------------------#
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

TRAIN_DATA_DIR = "training"
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B"
OUTPUT_DIR = "ppo_qwen_powl_generator_openai_reward"

MAX_PROMPT_TOKENS = 4096
MAX_COMPLETION_TOKENS = 4096
BATCH_SIZE = 4
MINI_BATCH_SIZE = 1
PPO_EPOCHS = 4
LEARNING_RATE = 1e-5
INIT_KL_COEF = 0.2
TARGET_KL = 6.0         # kept for reference only
GAMMA = 1.0
LAM = 0.95
CLIPRANGE = 0.2
CLIPRANGE_VALUE = 0.2
VF_COEF = 0.1
MAX_GRAD_NORM = 1.0
MAX_TRAINING_STEPS = 1000
MAX_DATASET_SAMPLES = 500

GENERATION_KWARGS = {
    "min_length": -1,
    "top_k": 0.0,
    "top_p": 1.0,
    "do_sample": True,
    "temperature": 0.7,
    "max_new_tokens": MAX_COMPLETION_TOKENS,
    "pad_token_id": None,  # filled in after tokenizer loads
    "eos_token_id": None,
}

LOG_WITH = None  # "wandb" | "tensorboard" | None
LOGGING_STEPS = 1
SAVE_STEPS = 100

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-4.1-mini"


# ---------------------------------------------------------------------------#
# 2. Prompt and Data Loading                                                  #
# ---------------------------------------------------------------------------#

def get_powl_prompt(description: str, activities: List[str]) -> str:
    activities_str = ", ".join([f"'{act}'" for act in activities])
    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) is a partially ordered graph representation of a process, extended with control-flow operators for modeling choice and loop structures. There are four types of POWL models:
- an activity (identified by its label, e.g., 'M'). Silent activities with empty labels (tau labels) are also supported.
- a choice of other POWL models (exclusive choice: X(A, B)).
- a loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit.
- a partial order: PO=(nodes={{...}}, order={{...}}), where order is a set of source-->target dependencies; unconnected nodes are concurrent.

Example code:
```python
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
A = Transition(label='A')
B = Transition(label='B')
C = Transition(label='C')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])
xor = OperatorPOWL(operator=Operator.XOR, children=[C, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
```

NOW, generate the POWL model for the process below.
DESCRIPTION: {description}
ACTIVITIES (use these exactly, same names): [{activities_str}]

Respond with valid Python code only, defining 'root'.
"""


def load_limited_dataset(data_dir: str, max_samples: int) -> Dataset:
    desc_folder = os.path.join(data_dir, "textual_descriptions")
    powl_folder = os.path.join(data_dir, "powl")
    if not os.path.exists(desc_folder) or not os.path.exists(powl_folder):
        raise FileNotFoundError(f"Data directories not found in '{data_dir}'.")
    file_names = [f for f in os.listdir(desc_folder) if f.endswith('.json')]
    random.shuffle(file_names)
    data_list = []
    for file_name in file_names[:max_samples]:
        base_name = os.path.splitext(file_name)[0]
        json_path = os.path.join(desc_folder, file_name)
        py_path = os.path.join(powl_folder, f"{base_name}.py")
        if not os.path.exists(py_path):
            continue
        with open(json_path, 'r', encoding='utf-8') as f:
            desc_data = json.load(f)
        with open(py_path, 'r', encoding='utf-8') as f:
            powl_code = f.read()
        prompt = get_powl_prompt(desc_data["description"], desc_data["activities"])
        data_list.append({"query": prompt, "reference_completion": powl_code})
    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)


# ---------------------------------------------------------------------------#
# 3. OpenAI Reward Function                                                    #
# ---------------------------------------------------------------------------#

def get_openai_grading_prompt(original_prompt: str, completions: List[str]) -> str:
    prompt_intro = f"""
You are an expert in process modeling. Your task is to evaluate Python code snippets that generate POWL models based on a given prompt.

## The original prompt was:

## {original_prompt}

I have received {len(completions)} responses. Please evaluate each response based on its correctness, completeness, and adherence to the prompt's requirements.
Provide a grade for each response on a scale from -1.0 to 1.0, where:

* 1.0: The generated code is perfect and accurately models the process description.
* 0.1 to 0.9: The code is acceptable but may have minor errors or inaccuracies.
* 0.0: The code is syntactically correct but functionally wrong or completely misses the point.
* -1.0: The code is terrible, syntactically incorrect, or completely irrelevant.

Here are the responses to grade:
"""
    responses_section = ""
    for i, response in enumerate(completions):
        responses_section += f"\n--- RESPONSE {i + 1} ---\n```python\n{response}\n```"
    prompt_outro = f"""
Please provide your evaluation in a single JSON object. The JSON should have a single key \"grades\", which is a list of floating-point numbers corresponding to each response. The number of grades in the list must be exactly {len(completions)}.

Example format:
{{
  "grades": [0.8, -0.5, 1.0]
}}

Now, provide the JSON output for the responses above.
"""
    return prompt_intro + responses_section + prompt_outro


def compute_rewards_from_openai(prompts: List[str], completions: List[str]) -> List[torch.Tensor]:
    BAD_REWARD = -1.0
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set.")
        return [torch.tensor(BAD_REWARD) for _ in completions]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    rewards = []
    for prompt, completion in zip(prompts, completions):
        grading_prompt = get_openai_grading_prompt(prompt, [completion])
        payload = {
            "model": OPENAI_MODEL,
            "messages": [{"role": "user", "content": grading_prompt}],
            "response_format": {"type": "json_object"},
            "temperature": 0.0
        }
        try:
            response = requests.post(OPENAI_API_URL, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            response_data = response.json()
            grades_str = response_data.get("choices", [{}])[0].get("message", {}).get("content", "{}")
            grades_json = json.loads(grades_str)
            grades = grades_json.get("grades")
            reward = float(grades[0]) if grades and len(grades) == 1 else BAD_REWARD
            print(f"Grade received: {reward}")
        except Exception as e:
            print(f"ERROR during OpenAI grading: {e}")
            reward = BAD_REWARD
        rewards.append(torch.tensor(reward))
    return rewards


# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and PPO Setup                                           #
# ---------------------------------------------------------------------------#
def collator(data):
    return {key: [d[key] for d in data] for key in data[0]}

print("\nInitializing tokenizer and models…")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token
GENERATION_KWARGS["pad_token_id"] = tokenizer.pad_token_id
GENERATION_KWARGS["eos_token_id"] = tokenizer.eos_token_id

dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)

# checkpoint handling ------------------------------------------------------- #
model_load_path = MODEL_NAME
resume_from_checkpoint = False
if os.path.isdir(OUTPUT_DIR):
    checkpoints = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if checkpoints:
        latest = max(checkpoints, key=lambda d: int(re.search(r"-(\d+)$", d).group(1)))
        model_load_path = os.path.join(OUTPUT_DIR, latest)
        resume_from_checkpoint = True
        print(f"✅ Resuming from checkpoint: {model_load_path}")
    else:
        print(f"🏁 No checkpoint found in '{OUTPUT_DIR}'. Starting fresh.")
else:
    print(f"🏁 Output directory '{OUTPUT_DIR}' not found. Starting fresh.")

# policy / reference -------------------------------------------------------- #
policy_model = AutoModelForCausalLMWithValueHead.from_pretrained(
    model_load_path, torch_dtype=torch.bfloat16, device_map="auto"
)
ref_model = AutoModelForCausalLMWithValueHead.from_pretrained(
    MODEL_NAME, torch_dtype=torch.bfloat16, device_map="auto"
)

# ---------------------------------------------------------------------------#
# 4-bis. Dummy Reward & Value models (required by PPOTrainer v2)  # NEW      #
# ---------------------------------------------------------------------------#
class ZeroRewardModel(torch.nn.Module):  # NEW
    """
    Minimal reward model that returns a zero scalar for any input.
    Needed only because PPOTrainer's new signature requires a Module.
    """
    def __init__(self):
        super().__init__()
        self.dummy = torch.nn.Parameter(torch.zeros(1))

    def forward(self, input_ids=None, **kwargs):
        batch = input_ids.shape[0] if input_ids is not None else 1
        logits = torch.zeros(batch, 1, device=self.dummy.device)
        return SequenceClassifierOutput(logits=logits)

reward_model = ZeroRewardModel()          # NEW
value_model = policy_model                # NEW (share weights with policy)

# ---------------------------------------------------------------------------#
# PPO v2 Configuration (only valid fields)                                   #
# ---------------------------------------------------------------------------#
ppo_config = PPOConfig(
    learning_rate=LEARNING_RATE,
    batch_size=BATCH_SIZE,
    mini_batch_size=MINI_BATCH_SIZE,
    num_ppo_epochs=PPO_EPOCHS,
    seed=SEED,
    gamma=GAMMA,
    lam=LAM,
    cliprange=CLIPRANGE,
    cliprange_value=CLIPRANGE_VALUE,
    vf_coef=VF_COEF,
    max_grad_norm=MAX_GRAD_NORM,
    kl_coef=INIT_KL_COEF,
    report_to=LOG_WITH,
    run_name="ppo_powl_generation",
)

# ---------------------------------------------------------------------------#
# Instantiate PPOTrainer v2 (new signature)                                  #
# ---------------------------------------------------------------------------#
ppo_trainer = PPOTrainer(
    args=ppo_config,
    processing_class=tokenizer,
    model=policy_model,
    ref_model=ref_model,
    reward_model=reward_model,
    train_dataset=dataset,
    value_model=value_model,
    data_collator=collator,
)

# ---------------------------------------------------------------------------#
# 5. Training Loop                                                            #
# ---------------------------------------------------------------------------#
print("\n--- Starting PPO training (TRL v0.22+) ---")
global_step = 0
best_reward = float('-inf')

for epoch in range(MAX_TRAINING_STEPS // BATCH_SIZE):
    print(f"\n--- Epoch {epoch + 1} ---")
    # 1) sample prompts ------------------------------------------------------ #
    batch_prompts = [random.choice(dataset)["query"] for _ in range(BATCH_SIZE)]
    query_tensors = [
        tokenizer(p, return_tensors="pt", truncation=True, padding=True, max_length=MAX_PROMPT_TOKENS).input_ids[0]
        for p in batch_prompts
    ]
    # 2) generate responses -------------------------------------------------- #
    responses_tensors = [
        ppo_trainer.generate(q.unsqueeze(0), return_prompt=False, **GENERATION_KWARGS).squeeze()
        for q in query_tensors
    ]
    responses = [tokenizer.decode(r, skip_special_tokens=True) for r in responses_tensors]

    # 3) get scalar rewards -------------------------------------------------- #
    rewards = compute_rewards_from_openai(batch_prompts, responses)
    avg_reward = float(torch.stack(rewards).mean())
    print(f"Average reward: {avg_reward:.3f}")
    if avg_reward > best_reward:
        best_reward = avg_reward
        print(f"🏆  New best average reward: {best_reward:.3f}")

    # 4) PPO optimisation step ---------------------------------------------- #
    stats = ppo_trainer.step(query_tensors, responses_tensors, rewards)
    global_step += BATCH_SIZE
    if global_step % LOGGING_STEPS == 0:
        print(f"Step {global_step}: "
              f"total_loss={stats['ppo/loss/total']:.4f}  "
              f"policy_loss={stats['ppo/loss/policy']:.4f}  "
              f"value_loss={stats['ppo/loss/value']:.4f}  "
              f"kl={stats['ppo/mean_non_score_reward']:.4f}")

    # 5) checkpoint ---------------------------------------------------------- #
    if global_step % SAVE_STEPS == 0:
        ckpt_dir = os.path.join(OUTPUT_DIR, f"checkpoint-{global_step}")
        print(f"💾 Saving checkpoint to {ckpt_dir}")
        ppo_trainer.save_pretrained(ckpt_dir)
        tokenizer.save_pretrained(ckpt_dir)

    if global_step >= MAX_TRAINING_STEPS:
        break

# ---------------------------------------------------------------------------#
# 6. Save final artefacts                                                    #
# ---------------------------------------------------------------------------#
print("\n🎉 Training finished.")
print(f"Best batch-average reward: {best_reward:.3f}")
final_dir = os.path.join(OUTPUT_DIR, "final_model")
print(f"💾 Saving final model to {final_dir}")
ppo_trainer.save_pretrained(final_dir)
tokenizer.save_pretrained(final_dir)
print("Done!")