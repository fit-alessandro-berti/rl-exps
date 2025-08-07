# sft_powl_generation.py

import os
import json
import random
import torch
import re
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, DataCollatorForLanguageModeling
from trl import SFTTrainer
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
MODEL_NAME = "./grpo_qwen_powl_generator_openai_reward"  # Starting model
OUTPUT_DIR = "sft_qwen_powl_generator"

# --- Training Hyperparameters ---
MAX_SEQ_LENGTH = 8192  # Combined prompt + completion max length
PER_DEVICE_BATCH = 1
GRAD_ACC_STEPS = 4
LEARNING_RATE = 2e-5  # Typically higher for SFT than GRPO
NUM_EPOCHS = 3  # SFT usually uses epochs instead of steps
MAX_DATASET_SAMPLES = 500

# --- Logging and Saving Configuration ---
LOGGING_STEPS = 10  # Print diagnostics every 10 steps
SAVE_STEPS = 100  # Save a checkpoint every 100 steps
EVAL_STEPS = 100  # Evaluate every 100 steps
WARMUP_STEPS = 100  # Warmup for learning rate scheduler


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


def load_sft_dataset(data_dir: str, max_samples: int) -> Dataset:
    """
    Loads data formatted for SFT training.
    Each example contains the full text (prompt + completion).
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

        # For SFT, we need the full conversation (prompt + response)
        # Format as a conversation that the model should learn
        full_text = f"{prompt}\n\n```python\n{powl_code}\n```"

        data_list.append({"text": full_text})

    print(f"Loaded {len(data_list)} samples for SFT training.")
    return Dataset.from_list(data_list)


# Split dataset into train and validation (90/10 split)
def split_dataset(dataset: Dataset, val_ratio: float = 0.1):
    """
    Split dataset into training and validation sets.
    """
    split = dataset.train_test_split(test_size=val_ratio, seed=SEED)
    return split["train"], split["test"]


# Load and prepare dataset
print("\nLoading dataset...")
full_dataset = load_sft_dataset(TRAIN_DATA_DIR, max_samples=MAX_DATASET_SAMPLES)
train_dataset, eval_dataset = split_dataset(full_dataset)
print(f"Training samples: {len(train_dataset)}, Validation samples: {len(eval_dataset)}")

# ---------------------------------------------------------------------------#
# 3. Model, Tokenizer, and Trainer Setup                                      #
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
tokenizer = AutoTokenizer.from_pretrained(model_load_path, use_fast=False)

# Set padding token if not already set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_load_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True  # In case the model needs custom code
)
print("Model and Tokenizer loaded successfully.")

# ---------------------------------------------------------------------------#
# 4. Training Arguments Configuration                                         #
# ---------------------------------------------------------------------------#

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    overwrite_output_dir=False,  # Don't overwrite, allows resuming
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=PER_DEVICE_BATCH,
    per_device_eval_batch_size=PER_DEVICE_BATCH,
    gradient_accumulation_steps=GRAD_ACC_STEPS,
    gradient_checkpointing=True,  # Saves memory
    optim="adamw_torch",
    learning_rate=LEARNING_RATE,
    warmup_steps=WARMUP_STEPS,
    logging_steps=LOGGING_STEPS,
    save_steps=SAVE_STEPS,
    eval_steps=EVAL_STEPS,
    evaluation_strategy="steps",
    save_strategy="steps",
    save_total_limit=3,  # Keep only last 3 checkpoints
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    bf16=True,  # Use bfloat16 precision
    tf32=True,  # Use tf32 on Ampere GPUs
    dataloader_num_workers=4,
    remove_unused_columns=True,
    push_to_hub=False,
    report_to="none",  # Can be "tensorboard", "wandb", etc.
    seed=SEED,
)


# ---------------------------------------------------------------------------#
# 5. SFT Trainer Setup                                                        #
# ---------------------------------------------------------------------------#

# Define a formatting function for the dataset
def formatting_func(examples):
    """
    This function is called by SFTTrainer to format the examples.
    It should return a list of strings (the full texts to train on).
    """
    return examples["text"]


trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    formatting_func=formatting_func,
    max_seq_length=MAX_SEQ_LENGTH,
    packing=False,  # Set to True if you want to pack multiple examples in one sequence
    dataset_text_field=None,  # We're using formatting_func instead
)

# ---------------------------------------------------------------------------#
# 6. Training Execution                                                       #
# ---------------------------------------------------------------------------#

print("\n" + "=" * 60)
print("--- Starting SFT Training ---")
print(f"Total training samples: {len(train_dataset)}")
print(f"Total validation samples: {len(eval_dataset)}")
print(f"Batch size: {PER_DEVICE_BATCH}")
print(f"Gradient accumulation steps: {GRAD_ACC_STEPS}")
print(f"Effective batch size: {PER_DEVICE_BATCH * GRAD_ACC_STEPS}")
print(f"Number of epochs: {NUM_EPOCHS}")
print(f"Learning rate: {LEARNING_RATE}")
print(f"Max sequence length: {MAX_SEQ_LENGTH}")
print(f"Logging every {LOGGING_STEPS} steps")
print(f"Saving checkpoint every {SAVE_STEPS} steps")
print(f"Evaluating every {EVAL_STEPS} steps")
print("=" * 60 + "\n")

# Train the model
trainer.train(resume_from_checkpoint=resume_from_checkpoint)

print("\n--- Training Finished ---")

# ---------------------------------------------------------------------------#
# 7. Save Final Model                                                        #
# ---------------------------------------------------------------------------#

# Save the final trained model and tokenizer
final_model_path = os.path.join(OUTPUT_DIR, "final_model")
trainer.save_model(final_model_path)
tokenizer.save_pretrained(final_model_path)
print(f"✅ Final model and tokenizer saved to {final_model_path}")

# Save training history
if hasattr(trainer.state, 'log_history'):
    import json

    history_path = os.path.join(OUTPUT_DIR, "training_history.json")
    with open(history_path, 'w') as f:
        json.dump(trainer.state.log_history, f, indent=2)
    print(f"📊 Training history saved to {history_path}")

print("\n🎉 SFT Training Complete!")
print(f"Model saved in: {OUTPUT_DIR}")
print("You can load the model with:")
print(f"  model = AutoModelForCausalLM.from_pretrained('{final_model_path}')")
print(f"  tokenizer = AutoTokenizer.from_pretrained('{final_model_path}')")