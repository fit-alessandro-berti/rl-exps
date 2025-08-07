#!/usr/bin/env python3
"""
POWL Model Evaluation Script
Computes activity similarity, code correctness, behavioral similarity, and reward.
Handles generated files with _sample_N suffix pattern.
"""

import os
import json
import re
import ast
import csv
import argparse
import pm4py
from pathlib import Path
from typing import Set, Tuple, Dict
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator


def get_powl_prompt(description: str, activities: list) -> str:
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


def extract_activities_from_prompt(prompt: str) -> Set[str]:
    """
    Extracts the expected activities from the prompt.
    """
    activities = set()
    match = re.search(r"ACTIVITIES.*?:\s*\[(.*?)\]", prompt, re.DOTALL)
    if match:
        activities_str = match.group(1)
        for activity in re.findall(r"'([^']+)'", activities_str):
            activities.add(activity)
    return activities


def extract_activities_from_code(code_str: str) -> Tuple[Set[str], bool]:
    """
    Extracts activities defined in the generated code.
    """
    activities = set()
    has_valid_syntax = True

    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    try:
        ast.parse(code_str)
        has_valid_syntax = True
        transition_pattern = r"Transition\s*\(\s*label\s*=\s*['\"]([^'\"]+)['\"]"
        for match in re.finditer(transition_pattern, code_str):
            activities.add(match.group(1))
    except SyntaxError:
        has_valid_syntax = False
        transition_pattern = r"Transition\s*\(\s*label\s*=\s*['\"]([^'\"]+)['\"]"
        for match in re.finditer(transition_pattern, code_str):
            activities.add(match.group(1))

    return activities, has_valid_syntax


def assess_code_correctness(code_str: str) -> float:
    """
    Assesses the correctness of the POWL Python code.
    Returns a score between 0 and 1.
    """
    score = 0.0

    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    # Check 1: Valid Python syntax (0.2 points)
    try:
        ast.parse(code_str)
        score += 0.2
    except SyntaxError:
        return score

    # Check 2: Has required imports (0.2 points)
    required_imports = ["pm4py", "StrictPartialOrder", "OperatorPOWL", "Transition"]
    import_count = sum(1 for imp in required_imports if imp in code_str)
    score += 0.2 * (import_count / len(required_imports))

    # Check 3: Defines 'root' variable (0.2 points)
    if re.search(r'\broot\s*=', code_str):
        score += 0.2

    # Check 4: Uses POWL constructors (0.2 points)
    powl_constructors = ["Transition", "SilentTransition", "OperatorPOWL", "StrictPartialOrder"]
    constructor_count = sum(1 for cons in powl_constructors if cons + "(" in code_str)
    if constructor_count > 0:
        score += min(0.2, 0.05 * constructor_count)

    # Check 5: Uses proper operator types (0.2 points)
    operators = ["Operator.XOR", "Operator.LOOP", "Operator.SEQUENCE", "Operator.PARALLEL"]
    if any(op in code_str for op in operators):
        score += 0.2

    return min(1.0, score)


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
        exec_globals = {
            "pm4py": pm4py,
            "StrictPartialOrder": StrictPartialOrder,
            "OperatorPOWL": OperatorPOWL,
            "Transition": Transition,
            "SilentTransition": SilentTransition,
            "Operator": Operator
        }
        exec(code_str, exec_globals, local_scope)
        return local_scope.get("root")
    except Exception:
        return None


def evaluate_model(prompt: str, generated_code: str, reference_code: str) -> Dict[str, float]:
    """
    Evaluates a single generated model against prompt and reference.
    Returns dictionary with all scores.
    """
    # Component 1: Activity Similarity
    expected_activities = extract_activities_from_prompt(prompt)
    generated_activities, _ = extract_activities_from_code(generated_code)

    activity_similarity = 0.0
    if expected_activities:
        intersection = expected_activities.intersection(generated_activities)
        union = expected_activities.union(generated_activities)
        if union:
            activity_similarity = len(intersection) / len(union)
        if expected_activities.issubset(generated_activities):
            activity_similarity = min(1.0, activity_similarity + 0.2)

    # Component 2: Code Correctness
    code_correctness = assess_code_correctness(generated_code)

    # Component 3: Behavioral Similarity
    behavioral_similarity = 0.0
    gen_powl = get_powl_object_from_code(generated_code)
    ref_powl = get_powl_object_from_code(reference_code)

    if gen_powl is not None and ref_powl is not None:
        try:
            behavioral_similarity = pm4py.behavioral_similarity(ref_powl, gen_powl)
        except Exception:
            behavioral_similarity = 0.1  # Small reward for executable code

    # Compute total score and reward
    total_score = (
            0.3 * activity_similarity +
            0.3 * code_correctness +
            0.4 * behavioral_similarity
    )

    reward = -1.0 + 2.0 * total_score

    return {
        'activity_similarity': activity_similarity,
        'code_correctness': code_correctness,
        'behavioral_similarity': behavioral_similarity,
        'reward': reward
    }


def extract_base_name(filename: str) -> str:
    """
    Extracts base name from generated filename.
    E.g., 'c4b38e75-a504-4414-83ea-160cc607139a_sample_1.py' -> 'c4b38e75-a504-4414-83ea-160cc607139a'
    """
    # Remove .py extension
    name = filename
    if name.endswith('.py'):
        name = name[:-3]

    # Remove _sample_N suffix using regex
    pattern = r'^(.+?)(?:_sample_\d+)?$'
    match = re.match(pattern, name)
    if match:
        return match.group(1)
    return name


def main():
    parser = argparse.ArgumentParser(description='Evaluate POWL model generation')
    parser.add_argument('prompt_dir', help='Directory containing prompts (textual_descriptions)')
    parser.add_argument('reference_dir', help='Directory containing reference POWL code')
    parser.add_argument('generated_dir', help='Directory containing generated POWL code')
    parser.add_argument('-o', '--output', default='evaluation_results.csv', help='Output CSV file')

    args = parser.parse_args()

    # Get all directories
    prompt_dir = Path(args.prompt_dir)
    reference_dir = Path(args.reference_dir)
    generated_dir = Path(args.generated_dir)

    if not all([prompt_dir.exists(), reference_dir.exists(), generated_dir.exists()]):
        print("Error: One or more directories do not exist")
        return 1

    results = []

    # Get all generated files
    generated_files = sorted(generated_dir.glob('*.py'))
    print(f"Found {len(generated_files)} generated files")

    # Group generated files by base name
    generated_by_base = {}
    for gen_file in generated_files:
        base_name = extract_base_name(gen_file.name)
        if base_name not in generated_by_base:
            generated_by_base[base_name] = []
        generated_by_base[base_name].append(gen_file)

    print(f"Found {len(generated_by_base)} unique base models with samples")

    # Process each base model
    for base_name, gen_files in generated_by_base.items():
        prompt_file = prompt_dir / f"{base_name}.json"
        reference_file = reference_dir / f"{base_name}.py"

        if not prompt_file.exists():
            print(f"Warning: prompt file not found for {base_name}")
            continue

        if not reference_file.exists():
            print(f"Warning: reference file not found for {base_name}")
            continue

        # Load prompt
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt_data = json.load(f)
            prompt = get_powl_prompt(prompt_data["description"], prompt_data["activities"])
        except Exception as e:
            print(f"Error loading prompt for {base_name}: {e}")
            continue

        # Load reference code
        try:
            with open(reference_file, 'r', encoding='utf-8') as f:
                reference_code = f.read()
        except Exception as e:
            print(f"Error loading reference for {base_name}: {e}")
            continue

        # Evaluate each sample for this base model
        for gen_file in gen_files:
            try:
                # Load generated code
                with open(gen_file, 'r', encoding='utf-8') as f:
                    generated_code = f.read()

                # Evaluate
                print(f"Evaluating {gen_file.name}...")
                scores = evaluate_model(prompt, generated_code, reference_code)
                scores['filename'] = gen_file.stem  # filename without .py
                scores['base_model'] = base_name
                results.append(scores)

            except Exception as e:
                print(f"Error evaluating {gen_file.name}: {e}")
                continue

    # Write results to CSV
    if results:
        with open(args.output, 'w', newline='') as f:
            fieldnames = ['filename', 'base_model', 'activity_similarity', 'code_correctness',
                          'behavioral_similarity', 'reward']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"\nResults saved to {args.output}")

        # Print summary
        print(f"\n=== SUMMARY ===")
        print(f"Files evaluated: {len(results)}")

        avg_activity = sum(r['activity_similarity'] for r in results) / len(results)
        avg_correctness = sum(r['code_correctness'] for r in results) / len(results)
        avg_behavioral = sum(r['behavioral_similarity'] for r in results) / len(results)
        avg_reward = sum(r['reward'] for r in results) / len(results)

        print(f"Avg Activity Similarity: {avg_activity:.3f}")
        print(f"Avg Code Correctness: {avg_correctness:.3f}")
        print(f"Avg Behavioral Similarity: {avg_behavioral:.3f}")
        print(f"Avg Reward: {avg_reward:.3f}")

        # Per base model statistics
        print(f"\n=== PER MODEL STATISTICS ===")
        base_models = {}
        for r in results:
            base = r['base_model']
            if base not in base_models:
                base_models[base] = []
            base_models[base].append(r['reward'])

        for base, rewards in list(base_models.items())[:5]:  # Show first 5
            avg = sum(rewards) / len(rewards)
            print(f"{base}: {len(rewards)} samples, avg reward: {avg:.3f}")

        if len(base_models) > 5:
            print(f"... and {len(base_models) - 5} more models")
    else:
        print("No files were evaluated")


if __name__ == '__main__':
    main()