import csv
import os
from pathlib import Path


def read_csv(file_path):

    path = Path(file_path)
    if not path.is_absolute():
        base = Path(__file__).resolve().parent.parent
        path = (base / file_path).resolve()

    data = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
