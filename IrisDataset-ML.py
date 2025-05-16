import requests
from typing import Dict
import csv
from collections import defaultdict

def parse_iris_row(row: list[str]) -> LabeledPoint:
    measurements = [float(value) for value in row[:-1]]
    label = row[:-1].split("-")[-1]
    return LabeledPoint(measurements, label)

with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]



data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

with open('iris.data', 'w') as f:
    f.write(data.text)