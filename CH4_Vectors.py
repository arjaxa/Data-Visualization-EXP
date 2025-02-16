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
    return [v_i + w_i for v_i, w_i in zip(v, w)]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
# to substract 2 vectors, substract the corresponding elements
def substract(v: vector, w: vector) -> vector:
    """substracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same lenght"
    return [v_i - w_i for v_i, w_i in zip(v, w)]
assert substract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]