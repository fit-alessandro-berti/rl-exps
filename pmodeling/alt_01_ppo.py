# ppo_powl_generation_openai_reward_fixed.py
import os
import json
import random
import re
import sys
import torch
import requests
from tqdm import tqdm
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import PPOConfig, PPOTrainer
# These imports from pm4py are necessary for the 'exec' environment, even if not directly used in the script
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# ---------------------------------------------------------------------------#
# 1. Configuration & Hyperparameters #
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

# --- Training Hyperparameters ---
MAX_PROMPT_TOKENS = 4096  # This is handled by the tokenizer's truncation
MAX_COMPLETION_TOKENS = 512  # Max tokens to generate for the POWL code
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 5e-6
KL_BETA = 0.1
MAX_TRAINING_STEPS = 1000
MAX_DATASET_SAMPLES = 500  # Set to None to use all available data

# --- Logging and Saving Configuration ---
LOGGING_STEPS = 10
SAVE_STEPS = 100

# --- OpenAI API Configuration ---
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-4-turbo"  # Or any preferred model like "gpt-4.1-mini"


# ---------------------------------------------------------------------------#
# 2. Prompt and Data Loading #
# ---------------------------------------------------------------------------#
def get_powl_prompt(description: str, activities: list[str]) -> str:
    """
    Formats the prompt with the process description and activities.
    """
    activities_str = ", ".join([f"'{act}'" for act in activities])
    return f"""Generate a POWL model for the following process, saving the final result in the variable 'root'.

A partially ordered workflow language (POWL) is a partially ordered graph representation of a process, extended with control-flow operators for modeling choice and loop structures. There are four types of POWL models:
- an activity (identified by its label, e.g., 'M' identifies the activity M). Silent activities with empty labels (tau labels) are also supported.
- a choice of other POWL models (exclusive choice: X(A, B}}.
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


def load_limited_dataset(data_dir: str, max_samples: int | None) -> Dataset:
    """
    Loads a limited number of samples into a standard Hugging Face Dataset.
    """
    desc_folder = os.path.join(data_dir, "textual_descriptions")
    powl_folder = os.path.join(data_dir, "powl")
    if not os.path.exists(desc_folder) or not os.path.exists(powl_folder):
        raise FileNotFoundError(f"Data directories not found in '{data_dir}'.")

    file_names = [f for f in os.listdir(desc_folder) if f.endswith('.json')]
    random.shuffle(file_names)

    if max_samples is not None:
        file_names = file_names[:max_samples]

    data_list = []
    for file_name in file_names:
        base_name = os.path.splitext(file_name)[0]
        json_path = os.path.join(desc_folder, file_name)
        py_path = os.path.join(powl_folder, f"{base_name}.py")

        if not os.path.exists(py_path):
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            desc_data = json.load(f)
        # We don't need the reference completion for PPO, only the prompt
        prompt = get_powl_prompt(desc_data["description"], desc_data["activities"])
        data_list.append({"query": prompt})

    print(f"Loaded {len(data_list)} samples into the dataset.")
    return Dataset.from_list(data_list)


# ---------------------------------------------------------------------------#
# 3. REWARD FUNCTION (using OpenAI API) #
# ---------------------------------------------------------------------------#
def get_openai_grading_prompt(prompts: list[str], completions: list[str]) -> str:
    """
    Creates the prompt for the OpenAI grading model, handling multiple prompt-completion pairs.
    """
    prompt_intro = f"""
You are an expert in process modeling. Your task is to evaluate Python code snippets that generate POWL models based on their corresponding prompts.
I have received {len(completions)} responses, each with its own prompt. Please evaluate each response based on its correctness, completeness, and adherence to its prompt's requirements.
Provide a grade for each response on a scale from -1.0 to 1.0, where:
- 1.0: The generated code is perfect and accurately models the process description.
- 0.1 to 0.9: The code is acceptable but may have minor errors or inaccuracies.
- 0.0: The code is syntactically correct but functionally wrong or completely misses the point.
- -1.0: The code is terrible, syntactically incorrect, or completely irrelevant.

Here are the prompts and responses to grade:
"""
    responses_section = ""
    for i, (prompt, response) in enumerate(zip(prompts, completions)):
        # Extract only the relevant parts of the prompt for the grader
        desc_match = re.search(r"DESCRIPTION: (.*?)\nACTIVITIES:", prompt, re.DOTALL)
        act_match = re.search(r"ACTIVITIES: \[(.*?)\]", prompt, re.DOTALL)
        clean_prompt = f"Description: {desc_match.group(1).strip()}\nActivities: [{act_match.group(1).strip()}]" if desc_match and act_match else prompt

        responses_section += f"""
--- PROMPT {i + 1} ---
{clean_prompt}

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


def openai_grading_reward_function(prompts: list[str], completions: list[str], batch_size: int) -> list[float]:
    """
    Calculates rewards by getting grades from the OpenAI API.
    """
    BAD_REWARD = -1.0
    if not completions:
        return []

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.stderr.write("ERROR: OPENAI_API_KEY environment variable not set.\n")
        return [BAD_REWARD] * len(completions)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    grading_prompt = get_openai_grading_prompt(prompts, completions)
    payload = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "user", "content": grading_prompt}],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
    }

    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=payload, timeout=90)
        response.raise_for_status()
        response_data = response.json()
        grades_str = response_data.get("choices", [{}])[0].get("message", {}).get("content", "{}")
        grades_json = json.loads(grades_str)
        grades = grades_json.get("grades")

        if grades is None or not isinstance(grades, list) or len(grades) != len(completions):
            sys.stderr.write(f"ERROR: OpenAI response was malformed. Received: {grades_str}\n")
            return [BAD_REWARD] * len(completions)

        # Log the grades received for this batch
        print(f"--- BATCH GRADES: {grades} ---")
        return [float(g) for g in grades]

    except requests.RequestException as e:
        sys.stderr.write(f"ERROR: OpenAI API request failed: {e}\n")
        return [BAD_REWARD] * len(completions)
    except (json.JSONDecodeError, KeyError, TypeError, IndexError) as e:
        sys.stderr.write(f"ERROR: Failed to parse OpenAI response: {e}. Response text: {response.text}\n")
        return [BAD_REWARD] * len(completions)


# ---------------------------------------------------------------------------#
# 4. Model, Tokenizer, and Trainer Setup #
# ---------------------------------------------------------------------------#

# --- Check for Checkpoints ---
model_load_path = MODEL_NAME
resume_from_checkpoint = None
start_step = 0

if os.path.isdir(OUTPUT_DIR):
    checkpoints = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("checkpoint-")]
    if checkpoints:
        # Find the checkpoint with the highest step number
        latest_checkpoint = max(checkpoints, key=lambda d: int(re.search(r'-(\d+)$', d).group(1)))
        model_load_path = os.path.join(OUTPUT_DIR, latest_checkpoint)
        resume_from_checkpoint = True  # Flag to indicate we are resuming
        match = re.search(r'-(\d+)$', model_load_path)
        if match:
            start_step = int(match.group(1))
        print(f"✅ Resuming training from checkpoint: {model_load_path} at step {start_step}")
    else:
        print(f"🏁 No checkpoint found in '{OUTPUT_DIR}'. Starting from base model: {MODEL_NAME}")
else:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"🏁 Output directory '{OUTPUT_DIR}' created. Starting from base model: {MODEL_NAME}")

# --- Load Model and Tokenizer ---
print("\nInitializing Tokenizer and Model...")
tokenizer = AutoTokenizer.from_pretrained(model_load_path, padding_side="left", use_fast=False, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_load_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)
print("Model and Tokenizer loaded successfully.")

# --- Load Dataset ---
dataset = load_limited_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)


def tokenize_function(examples):
    # Tokenize the query (prompt)
    return tokenizer(examples["query"], truncation=True, max_length=MAX_PROMPT_TOKENS)


tokenized_dataset = dataset.map(tokenize_function, batched=True)

# --- PPO Configuration ---
# CORRECTED: Renamed 'args' to 'config', 'kl_coef' to 'kl_penalty', removed invalid args
ppo_config = PPOConfig(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=PER_DEVICE_BATCH,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    learning_rate=LEARNING_RATE,
    kl_penalty=KL_BETA,  # CORRECTED from kl_coef
    remove_unused_columns=False,
    bf16=True,
    logging_steps=LOGGING_STEPS,
    report_to="none",
    batch_size=PER_DEVICE_BATCH,
    forward_batch_size=PER_DEVICE_BATCH
)

# --- PPO Trainer Initialization ---
# CORRECTED: Passed 'config' and 'tokenizer' correctly, removed unused 'reward_model' etc.
trainer = PPOTrainer(
    config=ppo_config,
    tokenizer=tokenizer,
    model=model,
    ref_model=None,  # ref_model is optional and will be created automatically
    dataset=tokenized_dataset,
)

# ---------------------------------------------------------------------------#
# 5. Training Execution #
# ---------------------------------------------------------------------------#
print("\n--- Starting PPO Training with OpenAI-based Rewards ---")
print(f"Logging diagnostics every {LOGGING_STEPS} steps.")
print(f"Saving model checkpoint every {SAVE_STEPS} steps.")

# --- Generation settings for the model ---
generation_kwargs = {
    "top_k": 0.0,
    "top_p": 1.0,
    "do_sample": True,
    "pad_token_id": tokenizer.pad_token_id,
    "eos_token_id": tokenizer.eos_token_id,
    "max_new_tokens": MAX_COMPLETION_TOKENS,
}

# --- The manual training loop ---
dataloader = trainer.dataloader
pbar = tqdm(total=MAX_TRAINING_STEPS, initial=start_step)
pbar.set_description("PPO Training")

# Fast-forward dataloader to the starting step
for _ in range(start_step):
    next(dataloader, None)

for step, batch in enumerate(dataloader, start=start_step):
    if step >= MAX_TRAINING_STEPS:
        break

    # Get the tokenized prompts
    query_tensors = batch["input_ids"].to(model.device)

    # Generate responses from the policy model
    # The generate method from PPOTrainer handles encoding and decoding
    response_tensors = trainer.generate(
        query_tensors,
        return_prompt=False,  # We only want the completion
        **generation_kwargs,
    )

    # Decode for the reward function and logging
    # batch['query'] is already available from the dataset
    # batch['response'] contains the decoded completion
    batch["response"] = tokenizer.batch_decode(response_tensors, skip_special_tokens=True)

    # Get rewards from the external API
    prompts = batch["query"]
    completions = batch["response"]
    rewards = openai_grading_reward_function(prompts, completions, ppo_config.batch_size)
    reward_tensors = [torch.tensor(reward, device=model.device) for reward in rewards]

    # Run PPO optimization step
    # The `step` method calculates the PPO loss and performs a gradient update
    stats = trainer.step([query_tensors[0]], [response_tensors[0]], reward_tensors)

    # Log the stats
    if step > 0 and step % LOGGING_STEPS == 0:
        log_stats = {f"ppo/{k}": v for k, v in stats.items()}
        log_stats["rewards/mean"] = torch.mean(torch.tensor(reward_tensors)).item()
        trainer.log_stats(log_stats, batch, reward_tensors)

    # Save model checkpoint
    if step > 0 and step % SAVE_STEPS == 0:
        save_path = os.path.join(OUTPUT_DIR, f"checkpoint-{step}")
        trainer.save_pretrained(save_path)
        print(f"\n--- Checkpoint saved at step {step} to {save_path} ---")

    pbar.update(1)

pbar.close()

# --- Final Save ---
print("\n--- Training Finished ---")
final_save_path = os.path.join(OUTPUT_DIR, "final_model")
trainer.save_pretrained(final_save_path)
print(f"Final model and tokenizer saved to {final_save_path}")
