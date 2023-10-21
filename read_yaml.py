import pandas as pd
import json
import yaml

def yaml_to_df(file: str):
    with open(file, "r") as f:
        json_file = json.dumps(yaml.safe_load(f))
    table = pd.read_json(json_file)
    return table

if __name__ == "__main__":
	print(yaml_to_df("yaml_example.yaml"))
