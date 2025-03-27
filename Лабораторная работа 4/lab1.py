import json

def task(filename: str) -> float:
    with open(filename, "r") as f:
        data = json.load(f)
    total_sum = sum(entry['score'] * entry['weight'] for entry in data)
    return round(total_sum, 3)

filename = 'input.json'
print(task(filename))
