#!/usr/bin/env python3
"""
POWL Code Correctness Evaluator
Evaluates the syntactic and structural correctness of POWL Python code files.
Produces a CSV report with detailed scoring breakdown.

Scoring System:
- Raw score: 0.0 to 1.0 (based on code quality checks)
- Mapped score: -1.0 to 1.0
  * Raw scores 0.00-0.75 map to -1.0 to 0.0
  * Raw scores 0.75-1.00 map to 0.0 to 1.0
  * This means only exceptionally good code (>75% raw) gets positive scores
"""

import os
import re
import ast
import csv
import argparse
from typing import Dict, List, Tuple
from pathlib import Path
import traceback


def map_score_to_range(score: float) -> float:
    """
    Maps a score from [0, 1] to [-1, 1] with special mapping:
    - [0.0, 0.75] maps to [-1.0, 0.0]
    - [0.75, 1.0] maps to [0.0, 1.0]
    """
    if score <= 0.75:
        # Map 0.0-0.75 to -1.0-0.0
        return (score / 0.75) - 1.0
    else:
        # Map 0.75-1.0 to 0.0-1.0
        return (score - 0.75) * 4.0


def assess_code_correctness(code_str: str) -> Dict[str, float]:
    """
    Assesses the correctness of the POWL Python code with detailed scoring.
    Returns a dictionary with individual scores and mapped total score (-1.0 to 1.0).
    """
    scores = {
        'syntax_valid': 0.0,
        'has_imports': 0.0,
        'defines_root': 0.0,
        'uses_constructors': 0.0,
        'uses_operators': 0.0,
        'raw_total': 0.0,
        'total': -1.0  # Mapped score from -1.0 to 1.0
    }

    # Clean code string
    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    # Check 1: Valid Python syntax (0.2 points)
    try:
        ast.parse(code_str)
        scores['syntax_valid'] = 0.2
    except SyntaxError:
        scores['total'] = -1.0  # Minimum score for invalid syntax
        return scores  # If syntax is invalid, return early

    # Check 2: Has required imports (0.2 points)
    required_imports = [
        "pm4py",
        "StrictPartialOrder",
        "OperatorPOWL",
        "Transition"
    ]
    import_count = sum(1 for imp in required_imports if imp in code_str)
    scores['has_imports'] = 0.2 * (import_count / len(required_imports))

    # Check 3: Defines 'root' variable (0.2 points)
    if re.search(r'\broot\s*=', code_str):
        scores['defines_root'] = 0.2

    # Check 4: Uses POWL constructors correctly (0.2 points)
    powl_constructors = [
        "Transition",
        "SilentTransition",
        "OperatorPOWL",
        "StrictPartialOrder"
    ]
    constructor_count = sum(1 for cons in powl_constructors if cons + "(" in code_str)
    if constructor_count > 0:
        scores['uses_constructors'] = min(0.2, 0.05 * constructor_count)

    # Check 5: Uses proper operator types (0.2 points)
    operators = ["Operator.XOR", "Operator.LOOP", "Operator.SEQUENCE", "Operator.PARALLEL"]
    if any(op in code_str for op in operators):
        scores['uses_operators'] = 0.2

    # Calculate raw total score (0.0 to 1.0)
    scores['raw_total'] = sum(v for k, v in scores.items() if k not in ['total', 'raw_total'])
    scores['raw_total'] = min(1.0, scores['raw_total'])

    # Map to -1.0 to 1.0 range
    scores['total'] = map_score_to_range(scores['raw_total'])

    return scores


def extract_activities_from_code(code_str: str) -> Tuple[List[str], bool]:
    """
    Extracts activities defined in the generated code.
    Returns a tuple of (activities_list, has_valid_syntax)
    """
    activities = []
    has_valid_syntax = True

    # Clean code string
    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    try:
        # Parse the code as AST to check syntax
        ast.parse(code_str)
        has_valid_syntax = True

        # Extract Transition labels using regex
        transition_pattern = r"Transition\s*\(\s*label\s*=\s*['\"]([^'\"]+)['\"]"
        for match in re.finditer(transition_pattern, code_str):
            activities.append(match.group(1))

    except SyntaxError:
        has_valid_syntax = False
        # Still try to extract activities with regex even if syntax is invalid
        transition_pattern = r"Transition\s*\(\s*label\s*=\s*['\"]([^'\"]+)['\"]"
        for match in re.finditer(transition_pattern, code_str):
            activities.append(match.group(1))

    return activities, has_valid_syntax


def count_powl_elements(code_str: str) -> Dict[str, int]:
    """
    Counts various POWL elements in the code.
    """
    elements = {
        'transitions': 0,
        'silent_transitions': 0,
        'operators': 0,
        'partial_orders': 0,
        'loops': 0,
        'xors': 0,
        'sequences': 0,
        'parallels': 0
    }

    # Clean code string
    code_str = code_str.strip()
    if code_str.startswith("```python"):
        code_str = code_str[len("```python"):].strip()
    if code_str.endswith("```"):
        code_str = code_str[:-len("```")].strip()

    # Count transitions
    elements['transitions'] = len(re.findall(r'Transition\s*\(', code_str))
    elements['silent_transitions'] = len(re.findall(r'SilentTransition\s*\(', code_str))

    # Count operators
    elements['operators'] = len(re.findall(r'OperatorPOWL\s*\(', code_str))
    elements['partial_orders'] = len(re.findall(r'StrictPartialOrder\s*\(', code_str))

    # Count specific operator types
    elements['loops'] = len(re.findall(r'Operator\.LOOP', code_str))
    elements['xors'] = len(re.findall(r'Operator\.XOR', code_str))
    elements['sequences'] = len(re.findall(r'Operator\.SEQUENCE', code_str))
    elements['parallels'] = len(re.findall(r'Operator\.PARALLEL', code_str))

    return elements


def evaluate_file(filepath: Path) -> Dict:
    """
    Evaluates a single Python file containing POWL code.
    """
    result = {
        'filename': filepath.name,
        'filepath': str(filepath),
        'file_size': 0,
        'line_count': 0,
        'error': None
    }

    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            code_str = f.read()

        result['file_size'] = len(code_str)
        result['line_count'] = code_str.count('\n') + 1

        # Get correctness scores
        scores = assess_code_correctness(code_str)
        result.update(scores)

        # Extract activities
        activities, has_valid_syntax = extract_activities_from_code(code_str)
        result['activities'] = ', '.join(activities) if activities else ''
        result['activity_count'] = len(activities)

        # Count POWL elements
        elements = count_powl_elements(code_str)
        result.update(elements)

    except Exception as e:
        result['error'] = str(e)
        # Set all scores to minimum on error
        for key in ['syntax_valid', 'has_imports', 'defines_root',
                    'uses_constructors', 'uses_operators', 'raw_total']:
            result[key] = 0.0
        result['total'] = -1.0  # Minimum mapped score

    return result


def evaluate_folder(folder_path: str, output_csv: str = None, pattern: str = "*.py"):
    """
    Evaluates all Python files in a folder and saves results to CSV.

    Args:
        folder_path: Path to folder containing Python files
        output_csv: Path for output CSV file (default: results.csv in same folder)
        pattern: File pattern to match (default: *.py)
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise ValueError(f"Folder {folder_path} does not exist")

    if output_csv is None:
        output_csv = folder / "evaluation_results.csv"
    else:
        output_csv = Path(output_csv)

    # Find all matching files
    files = list(folder.glob(pattern))
    if not files:
        print(f"No files matching pattern '{pattern}' found in {folder_path}")
        return

    print(f"Found {len(files)} files to evaluate")

    # Evaluate each file
    results = []
    for i, filepath in enumerate(files, 1):
        print(f"Evaluating {i}/{len(files)}: {filepath.name}")
        result = evaluate_file(filepath)
        results.append(result)

    # Write results to CSV
    if results:
        # Define column order
        columns = [
            'filename', 'filepath', 'file_size', 'line_count',
            'syntax_valid', 'has_imports', 'defines_root',
            'uses_constructors', 'uses_operators', 'raw_total', 'total',
            'activity_count', 'activities',
            'transitions', 'silent_transitions', 'operators', 'partial_orders',
            'loops', 'xors', 'sequences', 'parallels',
            'error'
        ]

        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(results)

        print(f"\nResults saved to: {output_csv}")

        # Print summary statistics
        print("\n=== SUMMARY STATISTICS ===")
        total_files = len(results)
        valid_syntax = sum(1 for r in results if r['syntax_valid'] > 0)
        defines_root = sum(1 for r in results if r['defines_root'] > 0)
        avg_score = sum(r['total'] for r in results) / total_files
        avg_raw_score = sum(r.get('raw_total', 0) for r in results) / total_files

        print(f"Total files evaluated: {total_files}")
        print(f"Files with valid syntax: {valid_syntax} ({valid_syntax / total_files * 100:.1f}%)")
        print(f"Files defining 'root': {defines_root} ({defines_root / total_files * 100:.1f}%)")
        print(f"Average raw score (0-1): {avg_raw_score:.3f}")
        print(f"Average mapped score (-1 to 1): {avg_score:.3f}")

        # Score distribution (using mapped scores)
        score_ranges = {
            '-1.0 to -0.5': 0,
            '-0.5 to 0.0': 0,
            '0.0 to 0.5': 0,
            '0.5 to 1.0': 0
        }

        for r in results:
            score = r['total']
            if score <= -0.5:
                score_ranges['-1.0 to -0.5'] += 1
            elif score <= 0.0:
                score_ranges['-0.5 to 0.0'] += 1
            elif score <= 0.5:
                score_ranges['0.0 to 0.5'] += 1
            else:
                score_ranges['0.5 to 1.0'] += 1

        print("\nMapped Score Distribution (-1 to 1):")
        for range_name, count in score_ranges.items():
            print(f"  {range_name}: {count} files ({count / total_files * 100:.1f}%)")

        # Additional insight: files at key thresholds
        exceptional_files = sum(1 for r in results if r['total'] > 0)
        good_files = sum(1 for r in results if r['total'] >= 0)

        print(f"\nKey Thresholds:")
        print(
            f"  Files with positive score (raw > 0.75): {exceptional_files} ({exceptional_files / total_files * 100:.1f}%)")
        print(f"  Files with non-negative score (raw >= 0.75): {good_files} ({good_files / total_files * 100:.1f}%)")

        # Score mapping explanation
        print(f"\nScore Mapping Reference:")
        print(f"  Raw 0.00 → Mapped -1.00 (worst)")
        print(f"  Raw 0.25 → Mapped -0.67")
        print(f"  Raw 0.50 → Mapped -0.33")
        print(f"  Raw 0.75 → Mapped  0.00 (threshold)")
        print(f"  Raw 0.88 → Mapped  0.50")
        print(f"  Raw 1.00 → Mapped  1.00 (best)")

        # Files with errors
        error_files = [r for r in results if r['error'] is not None]
        if error_files:
            print(f"\nFiles with errors: {len(error_files)}")
            for r in error_files[:5]:  # Show first 5 errors
                print(f"  - {r['filename']}: {r['error']}")
            if len(error_files) > 5:
                print(f"  ... and {len(error_files) - 5} more")


def main():
    parser = argparse.ArgumentParser(
        description='Evaluate POWL Python code files for correctness. '
                    'Scores range from -1.0 (worst) to 1.0 (best), '
                    'with 0.0 corresponding to 75% raw correctness.'
    )
    parser.add_argument(
        'folder',
        help='Path to folder containing Python files to evaluate'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output CSV file path (default: evaluation_results.csv in input folder)',
        default=None
    )
    parser.add_argument(
        '-p', '--pattern',
        help='File pattern to match (default: *.py)',
        default='*.py'
    )

    args = parser.parse_args()

    try:
        evaluate_folder(args.folder, args.output, args.pattern)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    exit(main())