import pandas as pd
import numpy as np
import os


def summarize_csvs(file_list, output_csv):
    summary = []

    for file in file_list:
        df = pd.read_csv(file)
        # Ensure reward_score is numeric
        df['reward_score'] = pd.to_numeric(df['reward_score'], errors='coerce')

        neg1_count = (df['reward_score'] == -1).sum()
        pos1_count = (df['reward_score'] == 1).sum()
        not_neg1_count = (df['reward_score'] != -1).sum()

        # Quantiles, ignoring -1
        valid_scores = df.loc[df['reward_score'] != -1, 'reward_score']
        quantiles = valid_scores.quantile([0, 0.25, 0.5, 0.75, 1]).values if not valid_scores.empty else [np.nan] * 5

        summary.append({
            'filename': os.path.basename(file),
            'reward_score = -1': neg1_count,
            'reward_score = 1': pos1_count,
            'reward_score != -1': not_neg1_count,
            'q0': quantiles[0],
            'q25': quantiles[1],
            'q50': quantiles[2],
            'q75': quantiles[3],
            'q100': quantiles[4]
        })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(output_csv, index=False)
    print(f'Summary written to {output_csv}')


# Example usage:
file_list = ['reward_scores_step0.csv', 'reward_scores_step1.csv', 'reward_scores_step2.csv', 'reward_scores_step3.csv', 'reward_scores_step4.csv', 'reward_scores_step5.csv']
output_csv = 'summary.csv'
summarize_csvs(file_list, output_csv)
