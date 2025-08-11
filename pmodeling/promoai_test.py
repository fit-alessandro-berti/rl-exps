import os
import pm4py
import pandas as pd

samples_dir = 'sampling_promoai_step2'
gt_dir = "test_promoai/xes"
root = None

log_dictio = {}
final_list = []

for file in os.listdir(samples_dir):
    label = file.split("_")[0]

    try:
        F = open(os.path.join(samples_dir, file), "r")
        content = F.read()
        exec(content)
        F.close()

        net, im, fm = pm4py.convert_to_petri_net(root)

        log_path = os.path.join(gt_dir, label+".xes")
        if log_path not in log_dictio:
            log = pm4py.read_xes(log_path, return_legacy_log_object=True)
            log_dictio[log_path] = log

        log = log_dictio[log_path]

        fitness = pm4py.fitness_token_based_replay(log, net, im, fm)["log_fitness"]
        precision = pm4py.precision_token_based_replay(log, net, im, fm)
    except:
        fitness = 0.0
        precision = 0.0

    f_score = (2*fitness*precision)/(fitness+precision) if (fitness+precision > 0) else 0.0

    final_list.append({"file": file, "label": label, "f_score": f_score, "fitness": fitness, "precision": precision})
    #break

final_list = pd.DataFrame(final_list)
final_list.to_csv("promoai_test.csv", index=False)

df2 = final_list.groupby("label")["f_score"].agg(["min", "max", "mean"])
df2.columns = ['min', 'max', 'mean']
df2.to_csv("promoai_test_agg.csv", index=True)  # Keep the label as index

