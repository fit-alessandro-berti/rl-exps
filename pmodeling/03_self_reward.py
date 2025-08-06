# grpo_powl_generation_self_reward.py

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
MODEL_NAME = "./grpo_qwen_powl_generator"  # Start from the model trained with simple rewards
OUTPUT_DIR = "grpo_qwen_powl_generator_self_reward"

# --- Training Hyperparameters ---
MAX_PROMPT_TOKENS = 4096
MAX_COMPLETION_TOKENS = 4096
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 5e-6
KL_BETA = 0.1
MAX_TRAINING_STEPS = 1000
NUM_GENERATIONS = 4
MAX_DATASET_SAMPLES = 500

# --- Logging and Saving Configuration ---
LOGGING_STEPS = 1  # Print diagnostics every step
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

def load_limited_dataset_no_reference(data_dir: str, max_samples: int) -> Dataset:
    """
    Loads a limited number of samples into a standard Hugging Face Dataset.
    Note: We don't load reference completions for self-reward training.
    """
    desc_folder = os.path.join(data_dir, "textual_descriptions")
    if not os.path.exists(desc_folder):
        raise FileNotFoundError(f"Data directory not found: '{desc_folder}'.")
    file_names = [f for f in os.listdir(desc_folder) if f.endswith('.json')]
    random.shuffle(file_names)
    data_list = []
    for file_name in file_names[:max_samples]:
        json_path = os.path.join(desc_folder, file_name)
        with open(json_path, 'r', encoding='utf-8') as f:
            desc_data = json.load(f)
        prompt = get_powl_prompt(desc_data["description"], desc_data["activities"])
        # Store activities for potential use in reward function
        data_list.append({"prompt": prompt, "activities": desc_data["activities"]})
    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)

dataset = load_limited_dataset_no_reference(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)

# ---------------------------------------------------------------------------#
# 3. Self-Reward Function                                                     #
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

def powl_self_reward_function(completions: List[str], **kwargs) -> List[float]:
    """
    Calculates rewards based on average behavioral similarity to other parsable outputs.
    No ground truth needed - completions are compared against each other.
    Returns a list of floats.
    """
    BAD_REWARD = -1.0
    
    # First, parse all completions and extract valid POWL objects
    powl_objects = []
    parsed_indices = []
    
    for i, gen_code in enumerate(completions):
        gen_code = gen_code.split("```python")[-1].split("```")[0]
        powl_obj = get_powl_object_from_code(gen_code)
        if powl_obj is not None:
            powl_objects.append(powl_obj)
            parsed_indices.append(i)
    
    print(f"Successfully parsed {len(powl_objects)} out of {len(completions)} completions")
    
    # Initialize rewards list with BAD_REWARD for all
    rewards = [BAD_REWARD] * len(completions)
    
    # If we have at least 2 parsable objects, compute similarities
    if len(powl_objects) >= 2:
        # For each parsable completion, compute average similarity to others
        for idx, i in enumerate(parsed_indices):
            current_powl = powl_objects[idx]
            similarities = []
            
            # Compare with all other parsable completions
            for other_idx, other_powl in enumerate(powl_objects):
                if idx != other_idx:  # Don't compare with itself
                    try:
                        similarity = pm4py.behavioral_similarity(current_powl, other_powl)
                        similarities.append(similarity)
                    except Exception as e:
                        # If similarity computation fails, skip this pair
                        print(f"Similarity computation failed between {idx} and {other_idx}: {e}")
                        continue
            
            # Calculate reward based on average similarity
            if similarities:
                avg_similarity = sum(similarities) / len(similarities)
                # Base reward for being parsable: 0.3
                # Similarity component: up to 0.7
                reward_score = 0.3 + 0.7 * avg_similarity
                # Convert to [-1, 1] range
                rewards[i] = -1.0 + 2.0 * reward_score
            else:
                # Parsable but couldn't compute similarity with any other
                rewards[i] = -0.5
    
    elif len(powl_objects) == 1:
        # Only one parsable object - give it a moderate reward for being valid
        idx = parsed_indices[0]
        rewards[idx] = 0.0  # Neutral reward
    
    # All non-parsable completions keep BAD_REWARD (-1.0)
    
    print(f"Rewards: {rewards}")
    return rewards

# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and Trainer Setup                                      #
# ---------------------------------------------------------------------------#

# Check for a local checkpoint to resume from
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
    reward_funcs=[powl_self_reward_function],
)

# ---------------------------------------------------------------------------#
# 5. Training Execution                                                       #
# ---------------------------------------------------------------------------#

print("\n--- Starting GRPO Training with Self-Reward ---")
print(f"Logging diagnostics every {LOGGING_STEPS} steps.")
print(f"Saving model checkpoint every {SAVE_STEPS} steps.")
print("Reward function: Average behavioral similarity to other generated outputs (no ground truth needed)")

# Pass the checkpoint path to trainer.train() to handle optimizer/scheduler states
trainer.train(resume_from_checkpoint=resume_from_checkpoint)

print("\n--- Training Finished ---")

# Save the final trained model
trainer.save_model(OUTPUT_DIR)
print(f"Final model and tokenizer saved to {OUTPUT_DIR}")