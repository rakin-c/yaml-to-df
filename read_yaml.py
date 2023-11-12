import pandas as pd
import json
import yaml

def read_yaml(file: str):
    with open(file, "r") as f:
        json_file = json.dumps(yaml.safe_load(f))
    df = pd.read_json(json_file)
    return df
