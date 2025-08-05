# grpo_powl_generation.py

import os
import json
import random
import torch
import pm4py
import traceback
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
MAX_COMPLETION_TOKENS = 512
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 5e-6
KL_BETA = 0.1
MAX_TRAINING_STEPS = 1000
NUM_GENERATIONS = 2
MAX_DATASET_SAMPLES = 500


# ---------------------------------------------------------------------------#
# 2. Prompt and Data Loading                                                  #
# ---------------------------------------------------------------------------#

def get_powl_prompt(description: str, activities: List[str]) -> str:
    """
    Formats the prompt with the process description and activities according to the specified template.
    """
    activities_str = ", ".join([f"'{act}'" for act in activities])

    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) is a partially ordered graph representation of a process, extended with control-flow operators for modeling choice and loop structures. There are four types of POWL models:
- an activity (identified by its label, e.g., 'M' identifies the activity M). Silent activities with empty labels (tau labels) are also supported.
- a choice of other POWL models (exclusive choice: X(A, B)).
- a loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit.
- a partial order: PO=(nodes={{...}}, order={{...}}), where order is a set of source-->target dependencies; unconnected nodes are concurrent.

Example 1: PO=(nodes={{NODE1, NODE2}}, order={{}})
Example 2: PO=(nodes={{NODE1, NODE2}}, order={{NODE1-->NODE2}})
Example 3: PO=(nodes={{NODE1, NODE2, NODE3, X(NODE4, NODE5)}}, order={{NODE1-->NODE2, NODE1-->X(NODE4, NODE5), NODE2-->X(NODE4, NODE5)}})

POWL classes in pm4py.objects.powl.obj:
- SilentTransition(): silent transition
- Transition(label): labeled transition
- StrictPartialOrder(nodes=[...]) with .order.add_edge(src, tgt)
- OperatorPOWL(operator=Operator.XOR or Operator.LOOP, children=[...])

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
    Loads a limited number of samples from the data directory into a Hugging Face Dataset.
    """
    desc_folder = os.path.join(data_dir, "textual_descriptions")
    powl_folder = os.path.join(data_dir, "powl")

    if not os.path.exists(desc_folder) or not os.path.exists(powl_folder):
        raise FileNotFoundError(f"Data directories not found in '{data_dir}'. Please ensure they exist.")

    file_names = [f for f in os.listdir(desc_folder) if f.endswith('.json')]
    random.shuffle(file_names)

    data_list = []
    for file_name in file_names:
        if len(data_list) >= max_samples:
            break

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

        data_list.append({
            "prompt": prompt,
            "reference_completion": powl_code
        })

    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)


dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)


# ---------------------------------------------------------------------------#
# 3. Reward Function                                                          #
# ---------------------------------------------------------------------------#

def get_powl_object_from_code(code_str: str):
    """
    Executes a Python code string and returns the 'root' POWL object.
    Returns None if execution fails or 'root' is not found.
    """
    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    try:
        local_scope = {}
        exec_globals = {
            "pm4py": pm4py,
            "StrictPartialOrder": StrictPartialOrder,
            "OperatorPOWL": OperatorPOWL,
            "Transition": Transition,
            "SilentTransition": SilentTransition,
            "Operator": Operator,
        }
        exec(code_str, exec_globals, local_scope)
        return local_scope.get("root")
    except Exception:
        return None


# --- REWARD FUNCTION (SIGNATURE CHANGED) ---
def powl_reward_function(completions: List[str], **kwargs) -> Dict[str, List[float]]:
    """
    Calculates a reward based on the behavioral similarity between the generated and reference POWL models.
    NOTE: The 'reference_completions' are passed via **kwargs by the trainer.
    """
    # Extract reference completions from kwargs, which is how the trainer passes extra columns.
    reference_completions = kwargs["reference_completions"]
    rewards = []

    for gen_code, ref_code in zip(completions, reference_completions):
        BAD_REWARD = -1.0

        ref_powl = get_powl_object_from_code(ref_code)
        gen_powl = get_powl_object_from_code(gen_code)

        if gen_powl is None or ref_powl is None:
            rewards.append(BAD_REWARD)
            continue

        reward_score = 0.0
        try:
            # 1. Reward for generating syntactically valid code that produces a POWL object
            reward_score += 0.25

            # Discover footprints for comparison
            ref_footprints = pm4py.discover_footprints(ref_powl)
            gen_footprints = pm4py.discover_footprints(gen_powl)

            # 2. Reward for using a subset of the correct activities
            if gen_footprints["activities"].issubset(ref_footprints["activities"]):
                reward_score += 0.25
                # Bonus for using the exact set of activities
                if gen_footprints["activities"] == ref_footprints["activities"]:
                    reward_score += 0.10

            # 3. Reward based on behavioral similarity
            similarity = pm4py.behavioral_similarity(ref_powl, gen_powl)
            reward_score += 0.40 * similarity

        except Exception:
            rewards.append(-0.5)  # Penalize pm4py errors
            continue

        # Scale reward from [0, 1] to [-1, 1] for the trainer
        final_reward = -1.0 + 2.0 * reward_score
        rewards.append(final_reward)

    return {"rewards": rewards}


# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and Trainer Setup                                      #
# ---------------------------------------------------------------------------#

print("Initializing Tokenizer and Model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
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
    remove_unused_columns=False,  # CRITICAL: Ensures 'reference_completion' is passed to reward function
    bf16=True,
    logging_steps=10,
    save_steps=100,
    report_to="none",
)

trainer = GRPOTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    reward_funcs=[powl_reward_function],  # Pass the reward function in a list
)

# ---------------------------------------------------------------------------#
# 5. Training Execution                                                       #
# ---------------------------------------------------------------------------#

print("Starting GRPO training...")
trainer.train()
print("Training finished.")

trainer.save_model(OUTPUT_DIR)
print(f"Final model and tokenizer saved to {OUTPUT_DIR}")
