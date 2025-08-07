import os
import csv
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# ---------------------------------------------------------------------------#
# 1. Configuration                                                            #
# ---------------------------------------------------------------------------#
SAMPLING_DIR = "sampling_sft"
TEST_POWL_DIR = "test/powl"
OUTPUT_CSV = "reward_scores_sft.csv"

# ---------------------------------------------------------------------------#
# 2. Helper Functions                                                         #
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
    except Exception as e:
        print(f"    Error parsing POWL: {e}")
        return None

def compute_reward_score(generated_code: str, reference_code: str) -> tuple:
    """
    Calculates reward based on behavioral similarity between generated and reference POWL models.
    Returns a tuple of (float reward score, int footprint count or None).
    """
    BAD_REWARD = -1.0
    PARTIAL_FAIL_REWARD = -0.5
    
    # Parse both POWL models
    ref_powl = get_powl_object_from_code(reference_code)
    gen_powl = get_powl_object_from_code(generated_code)
    
    if gen_powl is None or ref_powl is None:
        return BAD_REWARD, None
    
    try:
        reward_score = 0.6  # Base reward for valid POWL object
        footprint_count = None
        
        # Compare footprints
        ref_footprints = pm4py.discover_footprints(ref_powl)
        gen_footprints = pm4py.discover_footprints(gen_powl)
        
        # Check if generated activities are subset of reference
        if gen_footprints["activities"].issubset(ref_footprints["activities"]):
            reward_score += 0.1
            # Check if they're exactly the same
            if gen_footprints["activities"] == ref_footprints["activities"]:
                reward_score += 0.05
        
        # Compute behavioral similarity
        similarity = pm4py.behavioral_similarity(ref_powl, gen_powl)
        reward_score += 0.25 * similarity
        
        # Convert to [-1, 1] range as in original
        final_reward = -1.0 + 2.0 * reward_score
        
        # Calculate footprint count for correctly translated models (reward > threshold)
        if final_reward > 0:  # Consider positive reward as correctly translated
            sequence_count = len(gen_footprints.get("sequence", []))
            parallel_count = len(gen_footprints.get("parallel", []))
            footprint_count = sequence_count + parallel_count
        
        return final_reward, footprint_count
        
    except Exception as e:
        print(f"    Error computing similarity: {e}")
        return PARTIAL_FAIL_REWARD, None

# ---------------------------------------------------------------------------#
# 3. Main Processing                                                          #
# ---------------------------------------------------------------------------#

def main():
    if not os.path.exists(SAMPLING_DIR):
        print(f"Error: Sampling directory '{SAMPLING_DIR}' not found")
        return
    
    if not os.path.exists(TEST_POWL_DIR):
        print(f"Error: Test POWL directory '{TEST_POWL_DIR}' not found")
        return
    
    # Get all sample files
    sample_files = [f for f in os.listdir(SAMPLING_DIR) if f.endswith('.py')]
    print(f"Found {len(sample_files)} sample files to process")
    
    # Prepare results list
    results = []
    processed = 0
    errors = 0
    
    # Process each sample file
    for sample_file in sample_files:
        print(f"\nProcessing {sample_file}...")
        
        try:
            # Extract base name and sample number
            # Expected format: {base_name}_sample_{number}.py
            if '_sample_' not in sample_file:
                print(f"  Skipping: unexpected filename format")
                continue
            
            parts = sample_file.rsplit('_sample_', 1)
            base_name = parts[0]
            sample_num = parts[1].replace('.py', '')
            
            # Load generated sample
            sample_path = os.path.join(SAMPLING_DIR, sample_file)
            with open(sample_path, 'r', encoding='utf-8') as f:
                generated_code = f.read()
            
            # Load reference ground-truth
            reference_path = os.path.join(TEST_POWL_DIR, f"{base_name}.py")
            if not os.path.exists(reference_path):
                print(f"  Warning: Ground-truth file not found: {reference_path}")
                continue
            
            with open(reference_path, 'r', encoding='utf-8') as f:
                reference_code = f.read()
            
            # Compute reward score and footprint count
            reward, footprint_count = compute_reward_score(generated_code, reference_code)
            
            # Store result
            results.append({
                'base_name': base_name,
                'sample_number': sample_num,
                'sample_file': sample_file,
                'reward_score': reward,
                'footprint_count': footprint_count
            })
            
            footprint_str = f", Footprints: {footprint_count}" if footprint_count is not None else ""
            print(f"  Reward score: {reward:.4f}{footprint_str}")
            processed += 1
            
        except Exception as e:
            print(f"  Error processing {sample_file}: {e}")
            errors += 1
            continue
    
    # Write results to CSV
    if results:
        with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['base_name', 'sample_number', 'sample_file', 'reward_score', 'footprint_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in results:
                writer.writerow(row)
        
        print(f"\n✅ Processing complete!")
        print(f"  - Processed: {processed} files")
        print(f"  - Errors: {errors} files")
        print(f"  - Results saved to: {OUTPUT_CSV}")
        
        # Compute statistics
        rewards = [r['reward_score'] for r in results]
        avg_reward = sum(rewards) / len(rewards)
        min_reward = min(rewards)
        max_reward = max(rewards)
        
        print(f"\nReward Statistics:")
        print(f"  - Average: {avg_reward:.4f}")
        print(f"  - Min: {min_reward:.4f}")
        print(f"  - Max: {max_reward:.4f}")
        
        # Compute footprint statistics for correctly translated models
        footprint_counts = [r['footprint_count'] for r in results if r['footprint_count'] is not None]
        if footprint_counts:
            avg_footprints = sum(footprint_counts) / len(footprint_counts)
            min_footprints = min(footprint_counts)
            max_footprints = max(footprint_counts)
            
            print(f"\nFootprint Statistics (for correctly translated models):")
            print(f"  - Correctly translated: {len(footprint_counts)}/{len(results)} models")
            print(f"  - Average footprints: {avg_footprints:.2f}")
            print(f"  - Min footprints: {min_footprints}")
            print(f"  - Max footprints: {max_footprints}")
    else:
        print("\n⚠️ No results to save")

if __name__ == "__main__":
    main()
