from matplotlib import pyplot as plt
from typing import List

vector = list[float]

height_weight_age = [70, #inches
                     170, #pounds
                     40] #years

grades = [95, #ex1
          80, #ex2
          75, #ex3
          62] #ex4

def add(v: vector, w: vector) -> vector:
    """adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same lenght"
    return []