import os, shutil

POWL_FOLDER = os.path.join("..", "..", "pmodel-collection", "models", "o4-mini", "powl")
TD_FOLDER = os.path.join("..", "..", "pmodel-collection", "models", "textual_descriptions")

for index, file_name in enumerate(os.listdir(POWL_FOLDER)):
    powl_path = os.path.join(POWL_FOLDER, file_name)
    td_path = os.path.join(TD_FOLDER, file_name.replace(".py", ".json"))

    target = "training" if index < 1000 else "test"

    shutil.copy(powl_path, os.path.join(target, "powl", file_name))
    shutil.copy(td_path, os.path.join(target, "textual_descriptions", file_name.replace(".py", ".json")))
