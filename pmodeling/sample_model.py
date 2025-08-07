import os
import json
import random
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# ---------------------------------------------------------------------------#
# 1. Configuration                                                            #
# ---------------------------------------------------------------------------#
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

# --- Directory and Model Configuration ---
TEST_DATA_DIR = "test"
MODEL_PATH = "./grpo_qwen_powl_generator"  # Path to the trained model
OUTPUT_DIR = "sampling"
NUM_SAMPLES_PER_DESCRIPTION = 4  # Generate 4 samples per description
MAX_NEW_TOKENS = 4096
TEMPERATURE = 0.7
TOP_P = 0.9


# ---------------------------------------------------------------------------#
# 2. Prompt Function                                                          #
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


# ---------------------------------------------------------------------------#
# 3. Model Loading                                                            #
# ---------------------------------------------------------------------------#

print(f"Loading model from {MODEL_PATH}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, padding_side="left", use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
model.eval()  # Set to evaluation mode
print("Model loaded successfully.")


# ---------------------------------------------------------------------------#
# 4. Sampling Function                                                        #
# ---------------------------------------------------------------------------#

def generate_samples(prompt: str, num_samples: int) -> List[str]:
    """
    Generate multiple samples from the model for a given prompt.
    """
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    samples = []
    with torch.no_grad():
        for i in range(num_samples):
            outputs = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                temperature=TEMPERATURE,
                top_p=TOP_P,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id
            )

            # Decode the generated text
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract only the generated part (after the prompt)
            if prompt in generated_text:
                generated_code = generated_text[len(prompt):].strip()
            else:
                generated_code = generated_text.strip()

            samples.append(generated_code)
            print(f"  Sample {i + 1}/{num_samples} generated")

    return samples


def extract_code_from_response(response: str) -> str:
    """
    Extract Python code from the model's response.
    """
    # Try to extract code between ```python and ```
    if "```python" in response:
        parts = response.split("```python")
        if len(parts) > 1:
            code_part = parts[1].split("```")[0]
            return code_part.strip()

    # If no code blocks, assume the entire response is code
    return response.strip()


# ---------------------------------------------------------------------------#
# 5. Main Sampling Loop                                                       #
# ---------------------------------------------------------------------------#

def main():
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load test descriptions
    desc_folder = os.path.join(TEST_DATA_DIR, "textual_descriptions")
    if not os.path.exists(desc_folder):
        raise FileNotFoundError(f"Test descriptions directory not found: {desc_folder}")

    # Get all JSON files
    json_files = [f for f in os.listdir(desc_folder) if f.endswith('.json')]
    print(f"Found {len(json_files)} test descriptions")

    skipped_files = 0
    total_files = 0

    # Process each description
    for idx, json_file in enumerate(json_files, 1):
        base_name = os.path.splitext(json_file)[0]
        json_path = os.path.join(desc_folder, json_file)

        # Determine output sample files for this description
        output_filenames = [f"{base_name}_sample_{i + 1}.py" for i in range(NUM_SAMPLES_PER_DESCRIPTION)]
        output_paths = [os.path.join(OUTPUT_DIR, fname) for fname in output_filenames]
        existing_outputs = [os.path.exists(path) for path in output_paths]

        # If all sample files already exist, skip this description
        if all(existing_outputs):
            print(
                f"\n[{idx}/{len(json_files)}] Skipping {base_name}: all {NUM_SAMPLES_PER_DESCRIPTION} samples already exist.")
            skipped_files += 1
            continue

        print(f"\n[{idx}/{len(json_files)}] Processing {base_name}...")

        # Load description
        with open(json_path, 'r', encoding='utf-8') as f:
            desc_data = json.load(f)

        # Generate prompt
        prompt = get_powl_prompt(desc_data["description"], desc_data["activities"])

        # Generate only the number of *missing* samples
        num_samples_to_generate = NUM_SAMPLES_PER_DESCRIPTION - sum(existing_outputs)
        samples = generate_samples(prompt, num_samples_to_generate)

        # Save missing samples
        sample_iter = iter(samples)
        for sample_idx, (output_path, already_exists) in enumerate(zip(output_paths, existing_outputs), 1):
            if already_exists:
                print(f"  Skipping sample {sample_idx}: {os.path.basename(output_path)} already exists")
                continue
            # Extract code from response
            code = extract_code_from_response(next(sample_iter))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"  Saved sample {sample_idx} to {os.path.basename(output_path)}")
            total_files += 1

    print(
        f"\n✅ Sampling complete! {total_files} new samples generated, {skipped_files} descriptions skipped (all samples already existed).")
    print(f"Results saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
