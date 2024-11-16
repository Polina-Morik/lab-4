import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as input_file:
        python_file = json.load(input_file)
        result = [value["score"] * value["weight"] for value in python_file]
    return round(sum(result), 3)

print(task())
