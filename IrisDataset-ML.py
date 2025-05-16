import requests
from typing import Dict
from typing import NamedTuple
import csv
from collections import defaultdict
from matplotlib import pyplot as plt

class LabelPoint(NamedTuple):
    point: Vector
    label: str

def parse_iris_row(row: list[str]) -> LabeledPoint:
    measurements = [float(value) for value in row[:-1]]
    label = row[:-1].split("-")[-1]
    return LabeledPoint(measurements, label)

with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]

points_by_species: Dict[str, list[Vector]] == defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

with open('iris.data', 'w') as f:
    f.write(data.text)