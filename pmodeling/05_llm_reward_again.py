# grpo_powl_generation_openai_reward_fixed.py

import os
import json
import random
import torch
import pm4py
import re
import requests
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
MODEL_NAME = "./grpo_qwen_powl_generator"
OUTPUT_DIR = "grpo_qwen_powl_generator_step5"

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
        data_list.append({"prompt": prompt, "reference_completion": powl_code})
    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)


dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)


# ---------------------------------------------------------------------------#
# 3. NEW REWARD FUNCTION (using OpenAI API)                                   #
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


def openai_grading_reward_function(completions: List[str], **kwargs) -> List[float]:
    """
    Calculates rewards by getting grades from the OpenAI API.
    """
    BAD_REWARD = -1.0

    # --- FIX ---
    # The GRPOTrainer passes prompts under the `prompts` key.
    # We also add a print statement to see all available keys for easier debugging.
    # print(f"DEBUG: kwargs keys available in reward function: {kwargs.keys()}")

    # The `prompts` list will contain NUM_GENERATIONS identical prompts. We just need one.
    try:
        original_prompt = kwargs["prompts"][0]
    except KeyError:
        print("ERROR: Could not find 'prompts' key in kwargs. Unable to create grading prompt.")
        return [BAD_REWARD] * len(completions)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set.")
        return [BAD_REWARD] * len(completions)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    grading_prompt = get_openai_grading_prompt(original_prompt, completions)

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

        if grades is None or not isinstance(grades, list) or len(grades) != len(completions):
            print(f"ERROR: OpenAI response was malformed. Received: {grades_str}")
            return [BAD_REWARD] * len(completions)

        # --- MODIFIED --- Print grades obtained in the current iteration
        print(f"--- GRADES FOR STEP: {grades} ---")
        return [float(g) for g in grades]

    except requests.RequestException as e:
        print(f"ERROR: OpenAI API request failed: {e}")
        return [BAD_REWARD] * len(completions)
    except (json.JSONDecodeError, KeyError, TypeError, IndexError) as e:
        print(f"ERROR: Failed to parse OpenAI response: {e}. Response text: {response.text}")
        return [BAD_REWARD] * len(completions)


# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and Trainer Setup                                      #
# ---------------------------------------------------------------------------#

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
    reward_funcs=[openai_grading_reward_function],
)

# ---------------------------------------------------------------------------#
# 5. Training Execution                                                       #
# ---------------------------------------------------------------------------#

print("\n--- Starting GRPO Training with OpenAI-based Rewards ---")
print(f"Logging diagnostics every {LOGGING_STEPS} steps.")
print(f"Saving model checkpoint every {SAVE_STEPS} steps.")
print("Look for 'loss', 'rewards/chosen', 'rewards/rejected', and 'GRADES FOR STEP' in the logs below.")

trainer.train(resume_from_checkpoint=resume_from_checkpoint)

print("\n--- Training Finished ---")

trainer.save_model(OUTPUT_DIR)
print(f"Final model and tokenizer saved to {OUTPUT_DIR}")
