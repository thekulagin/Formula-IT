# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    return float(f"{sum([elem["score"] * elem["weight"] for elem in json_data]):.3f}")

print(task())
