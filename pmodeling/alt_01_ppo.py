# ppo_powl_generation_openai_reward.py

import os
import json
import random
import torch
import pm4py
import re
import requests
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import PPOConfig, PPOTrainer, AutoModelForCausalLMWithValueHead
from trl.core import LengthSampler
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from typing import List, Dict
import numpy as np

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
OUTPUT_DIR = "ppo_qwen_powl_generator_openai_reward"

# --- PPO Training Hyperparameters ---
MAX_PROMPT_TOKENS = 4096
MAX_COMPLETION_TOKENS = 4096
BATCH_SIZE = 4  # Number of experiences to collect before update
MINI_BATCH_SIZE = 1  # Size of minibatches for optimization
PPO_EPOCHS = 4  # Number of optimization epochs per batch
LEARNING_RATE = 1e-5
KL_PENALTY = "kl"  # Type of KL penalty: "kl", "abs", or "mse"
INIT_KL_COEF = 0.2  # Initial KL penalty coefficient
TARGET_KL = 6.0  # Target KL divergence
GAMMA = 1.0  # Discount factor
LAM = 0.95  # GAE lambda
CLIPRANGE = 0.2  # PPO clipping parameter
CLIPRANGE_VALUE = 0.2  # Value function clipping parameter
VF_COEF = 0.1  # Value function coefficient
MAX_GRAD_NORM = 1.0  # Gradient clipping
MAX_TRAINING_STEPS = 1000
MAX_DATASET_SAMPLES = 500

# --- Generation Configuration ---
GENERATION_KWARGS = {
    "min_length": -1,
    "top_k": 0.0,
    "top_p": 1.0,
    "do_sample": True,
    "temperature": 0.7,
    "max_new_tokens": MAX_COMPLETION_TOKENS,
    "pad_token_id": None,  # Will be set from tokenizer
    "eos_token_id": None,  # Will be set from tokenizer
}

# --- Logging and Saving Configuration ---
LOG_WITH = None  # Can be "wandb", "tensorboard", or None
LOGGING_STEPS = 1
SAVE_STEPS = 100

# --- OpenAI API Configuration ---
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-4.1-mini"


# ---------------------------------------------------------------------------#
# 2. Prompt and Data Loading                                                  #
# ---------------------------------------------------------------------------#

def get_powl_prompt(description: str, activities: List[str]) -> str:
    """
    Formats the prompt with the process description and activities.
    """
    activities_str = ", ".join([f"'{act}'" for act in activities])
    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) is a partially ordered graph representation of a process, extended with control-flow operators for modeling choice and loop structures. There are four types of POWL models:
- an activity (identified by its label, e.g., 'M' identifies the activity M). Silent activities with empty labels (tau labels) are also supported.
- a choice of other POWL models (exclusive choice: X(A, B)).
- a loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit.
- a partial order: PO=(nodes={{...}}, order={{...}}), where order is a set of source-->target dependencies; unconnected nodes are concurrent.

Example code:```python
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
    """
    Loads a limited number of samples into a standard Hugging Face Dataset.
    """
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
# 3. OpenAI Reward Function                                                   #
# ---------------------------------------------------------------------------#

def get_openai_grading_prompt(original_prompt: str, completions: List[str]) -> str:
    """
    Creates the prompt for the OpenAI grading model.
    """
    prompt_intro = f"""
You are an expert in process modeling. Your task is to evaluate Python code snippets that generate POWL models based on a given prompt.

The original prompt was:
---
{original_prompt}
---

I have received {len(completions)} responses. Please evaluate each response based on its correctness, completeness, and adherence to the prompt's requirements.
Provide a grade for each response on a scale from -1.0 to 1.0, where:
- 1.0: The generated code is perfect and accurately models the process description.
- 0.1 to 0.9: The code is acceptable but may have minor errors or inaccuracies.
- 0.0: The code is syntactically correct but functionally wrong or completely misses the point.
- -1.0: The code is terrible, syntactically incorrect, or completely irrelevant.

Here are the responses to grade:
"""

    responses_section = ""
    for i, response in enumerate(completions):
        responses_section += f"""
--- RESPONSE {i + 1} ---
```python
{response}
```
"""

    prompt_outro = f"""
Please provide your evaluation in a single JSON object. The JSON should have a single key "grades", which is a list of floating-point numbers corresponding to each response. The number of grades in the list must be exactly {len(completions)}.

Example format:
{{
  "grades": [0.8, -0.5, 1.0]
}}

Now, provide the JSON output for the responses above.
"""
    return prompt_intro + responses_section + prompt_outro


def compute_rewards_from_openai(prompts: List[str], completions: List[str]) -> List[torch.Tensor]:
    """
    Computes rewards for completions using OpenAI API.
    Returns a list of scalar tensors.
    """
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

    # Process each prompt-completion pair
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

            if grades is None or not isinstance(grades, list) or len(grades) != 1:
                print(f"ERROR: OpenAI response was malformed. Received: {grades_str}")
                reward = BAD_REWARD
            else:
                reward = float(grades[0])
                print(f"Grade received: {reward}")

        except requests.RequestException as e:
            print(f"ERROR: OpenAI API request failed: {e}")
            reward = BAD_REWARD
        except (json.JSONDecodeError, KeyError, TypeError, IndexError) as e:
            print(f"ERROR: Failed to parse OpenAI response: {e}")
            reward = BAD_REWARD

        rewards.append(torch.tensor(reward))

    return rewards


# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and PPO Setup                                         #
# ---------------------------------------------------------------------------#

def collator(data):
    """
    Collator function for PPO training.
    """
    return {key: [d[key] for d in data] for key in data[0]}


print("\nInitializing Tokenizer and Models...")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

# Update generation kwargs with tokenizer info
GENERATION_KWARGS["pad_token_id"] = tokenizer.pad_token_id
GENERATION_KWARGS["eos_token_id"] = tokenizer.eos_token_id

# Load dataset
dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)

# Check for existing checkpoint
model_load_path = MODEL_NAME
resume_from_checkpoint = False
if os.path.isdir(OUTPUT_DIR):
    checkpoints = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if checkpoints:
        latest_checkpoint = max(checkpoints, key=lambda d: int(re.search(r'-(\d+)$', d).group(1)))
        model_load_path = os.path.join(OUTPUT_DIR, latest_checkpoint)
        resume_from_checkpoint = True
        print(f"✅ Found checkpoint: {model_load_path}")
    else:
        print(f"🏁 No checkpoint found in '{OUTPUT_DIR}'. Starting from base model: {MODEL_NAME}")
else:
    print(f"🏁 Output directory '{OUTPUT_DIR}' not found. Starting from base model: {MODEL_NAME}")

# Load model with value head for PPO
model = AutoModelForCausalLMWithValueHead.from_pretrained(
    model_load_path,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Create reference model (frozen copy for KL divergence)
ref_model = AutoModelForCausalLMWithValueHead.from_pretrained(
    MODEL_NAME,  # Always use base model as reference
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

print("Model and Reference Model loaded successfully.")

# PPO Configuration
# PPO v2 configuration ------------------------------------------------------ #
# Only fields that still exist in the 0.22‑series API are kept.
ppo_config = PPOConfig(
    learning_rate=LEARNING_RATE,
    batch_size=BATCH_SIZE,
    mini_batch_size=MINI_BATCH_SIZE,
    num_ppo_epochs=PPO_EPOCHS,
    seed=SEED,
    # RL‑specific
    gamma=GAMMA,
    lam=LAM,
    cliprange=CLIPRANGE,
    cliprange_value=CLIPRANGE_VALUE,
    vf_coef=VF_COEF,
    max_grad_norm=MAX_GRAD_NORM,
    kl_coef=INIT_KL_COEF,
    # Logging
    report_to=LOG_WITH,
    run_name="ppo_powl_generation",
)

# Initialise PPO v2 Trainer ----------------------------------------------- #
# • first positional arg is the **PPOConfig** (now called “args”)
# • tokenizer is passed as `processing_class`
# • dataset is now `train_dataset`
# • reward_model & value_model can be left to None when you provide
#   your own reward signal, as you do with the OpenAI grader.
ppo_trainer = PPOTrainer(
    args=ppo_config,                 # <- renamed
    processing_class=tokenizer,      # <- was `tokenizer=`
    model=model,
    ref_model=ref_model,
    reward_model=None,               # we compute rewards externally
    train_dataset=dataset,           # <- was `dataset=`
    data_collator=collator,
)

# ---------------------------------------------------------------------------#
# 5. Training Loop                                                            #
# ---------------------------------------------------------------------------#

print("\n--- Starting PPO Training with OpenAI-based Rewards ---")
print(f"Training for {MAX_TRAINING_STEPS} steps")
print(f"Batch size: {BATCH_SIZE}, Mini-batch size: {MINI_BATCH_SIZE}")
print(f"PPO epochs per update: {PPO_EPOCHS}")

# Track training progress
global_step = 0
best_reward = float('-inf')

# Main training loop
for epoch in range(MAX_TRAINING_STEPS // BATCH_SIZE):
    print(f"\n--- Epoch {epoch + 1} ---")

    # Sample a batch of queries
    batch = []
    for _ in range(BATCH_SIZE):
        sample = random.choice(dataset)
        batch.append(sample["query"])

    # Tokenize queries
    query_tensors = []
    for query in batch:
        encoded = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=MAX_PROMPT_TOKENS)
        query_tensors.append(encoded.input_ids[0])

    # Generate responses
    print("Generating responses...")
    response_tensors = []
    for query_tensor in query_tensors:
        generation = ppo_trainer.generate(
            query_tensor.unsqueeze(0),
            return_prompt=False,
            **GENERATION_KWARGS
        )
        response_tensors.append(generation.squeeze())

    # Decode responses
    responses = [tokenizer.decode(r, skip_special_tokens=True) for r in response_tensors]

    # Compute rewards using OpenAI API
    print("Computing rewards from OpenAI...")
    rewards = compute_rewards_from_openai(batch, responses)

    # Log average reward
    avg_reward = sum([r.item() for r in rewards]) / len(rewards)
    print(f"Average reward for batch: {avg_reward:.3f}")

    # Track best reward
    if avg_reward > best_reward:
        best_reward = avg_reward
        print(f"New best average reward: {best_reward:.3f}")

    # Run PPO update
    print("Running PPO optimization...")
    stats = ppo_trainer.step(query_tensors, response_tensors, rewards)

    # Log statistics
    global_step += BATCH_SIZE
    if global_step % LOGGING_STEPS == 0:
        print(f"Step {global_step}: Loss={stats['ppo/loss/total']:.4f}, "
              f"Policy Loss={stats['ppo/loss/policy']:.4f}, "
              f"Value Loss={stats['ppo/loss/value']:.4f}, "
              f"Mean KL={stats['ppo/mean_non_score_reward']:.4f}")

    # Save checkpoint
    if global_step % SAVE_STEPS == 0:
        checkpoint_dir = os.path.join(OUTPUT_DIR, f"checkpoint-{global_step}")
        print(f"Saving checkpoint to {checkpoint_dir}")
        ppo_trainer.save_pretrained(checkpoint_dir)
        tokenizer.save_pretrained(checkpoint_dir)

    # Check if we've reached max steps
    if global_step >= MAX_TRAINING_STEPS:
        break

# ---------------------------------------------------------------------------#
# 6. Save Final Model                                                         #
# ---------------------------------------------------------------------------#

print("\n--- Training Finished ---")
print(f"Best average reward achieved: {best_reward:.3f}")

# Save final model
final_model_dir = os.path.join(OUTPUT_DIR, "final_model")
print(f"Saving final model to {final_model_dir}")
ppo_trainer.save_pretrained(final_model_dir)
tokenizer.save_pretrained(final_model_dir)

print("Training complete!")
