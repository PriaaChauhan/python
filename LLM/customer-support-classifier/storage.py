import json
from pathlib import Path

RESULTS_FILE = Path("data/results.json")


def save_result(data):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)

    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            results = json.load(file)
    else:
        results = []

    results.append(data)

    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)