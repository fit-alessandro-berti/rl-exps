# grpo_powl_generation.py

import os
import json
import random
import torch
import pm4py
import re
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import GRPOConfig, GRPOTrainer
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from typing import List, Dict

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
MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
OUTPUT_DIR = "grpo_qwen_powl_generator"

# --- Training Hyperparameters ---
MAX_PROMPT_TOKENS = 1024
MAX_COMPLETION_TOKENS = 4096
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 5e-6
KL_BETA = 0.1
MAX_TRAINING_STEPS = 1000
NUM_GENERATIONS = 2
MAX_DATASET_SAMPLES = 500

# --- NEW: Logging and Saving Configuration ---
LOGGING_STEPS = 1  # Print diagnostics every 10 steps
SAVE_STEPS = 100    # Save a checkpoint every 100 steps


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
        data_list.append({"prompt": prompt, "reference_completion": powl_code})
    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)

dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)

# ---------------------------------------------------------------------------#
# 3. Reward Function                                                          #
# ---------------------------------------------------------------------------#

def get_powl_object_from_code(code_str: str):
    """
    Executes a Python code string and returns the 'root' POWL object.
    """
    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()
    try:
        local_scope = {}
        exec_globals = {"pm4py": pm4py, "StrictPartialOrder": StrictPartialOrder, "OperatorPOWL": OperatorPOWL, "Transition": Transition, "SilentTransition": SilentTransition, "Operator": Operator}
        exec(code_str, exec_globals, local_scope)
        return local_scope.get("root")
    except Exception:
        return None

def powl_reward_function(completions: List[str], **kwargs) -> List[float]:
    """
    Calculates rewards based on behavioral similarity. Returns a list of floats.
    """
    reference_completions = kwargs["reference_completion"]
    rewards = []
    for gen_code, ref_code in zip(completions, reference_completions):
        gen_code = gen_code.split("```python")[-1].split("```")[0]
        print(gen_code)

        BAD_REWARD, PARTIAL_FAIL_REWARD = -1.0, -0.5
        ref_powl = get_powl_object_from_code(ref_code)
        gen_powl = get_powl_object_from_code(gen_code)
        if gen_powl is None or ref_powl is None:
            rewards.append(BAD_REWARD)
            continue
        try:
            reward_score = 0.25  # Base reward for valid POWL object
            ref_footprints = pm4py.discover_footprints(ref_powl)
            gen_footprints = pm4py.discover_footprints(gen_powl)
            if gen_footprints["activities"].issubset(ref_footprints["activities"]):
                reward_score += 0.25
                if gen_footprints["activities"] == ref_footprints["activities"]:
                    reward_score += 0.10
            similarity = pm4py.behavioral_similarity(ref_powl, gen_powl)
            reward_score += 0.40 * similarity
            rewards.append(-1.0 + 2.0 * reward_score)
        except Exception:
            rewards.append(PARTIAL_FAIL_REWARD)
    return rewards

# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and Trainer Setup                                      #
# ---------------------------------------------------------------------------#

# --- NEW: Check for a local checkpoint to resume from ---
model_load_path = MODEL_NAME
resume_from_checkpoint = None
if os.path.isdir(OUTPUT_DIR):
    checkpoints = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if checkpoints:
        latest_checkpoint = max(checkpoints, key=lambda d: int(re.search(r'-(\d+)$', d).group(1)))
        model_load_path = os.path.join(OUTPUT_DIR, latest_checkpoint)
        resume_from_checkpoint = model_load_path
        print(f"✅ Resuming training from checkpoint: {model_load_path}")
    else:
        print(f"🏁 No checkpoint found in '{OUTPUT_DIR}'. Starting from base model: {MODEL_NAME}")
else:
    print(f"🏁 Output directory '{OUTPUT_DIR}' not found. Starting from base model: {MODEL_NAME}")


print("\nInitializing Tokenizer and Model...")
tokenizer = AutoTokenizer.from_pretrained(model_load_path, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_load_path,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
print("Model and Tokenizer loaded successfully.")

training_args = GRPOConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=PER_DEVICE_BATCH,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    learning_rate=LEARNING_RATE,
    beta=KL_BETA,
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

trainer = GRPOTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    reward_funcs=[powl_reward_function],
)

# ---------------------------------------------------------------------------#
# 5. Training Execution                                                       #
# ---------------------------------------------------------------------------#

print("\n--- Starting GRPO Training ---")
print(f"Logging diagnostics every {LOGGING_STEPS} steps.")
print(f"Saving model checkpoint every {SAVE_STEPS} steps.")
print("Look for 'loss', 'rewards/chosen', and 'rewards/rejected' in the logs below.")

# Pass the checkpoint path to trainer.train() to handle optimizer/scheduler states
trainer.train(resume_from_checkpoint=resume_from_checkpoint)

print("\n--- Training Finished ---")

# Save the final trained model
trainer.save_model(OUTPUT_DIR)
print(f"Final model and tokenizer saved to {OUTPUT_DIR}")
