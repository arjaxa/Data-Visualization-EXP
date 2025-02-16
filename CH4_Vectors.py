
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

# 2

def vector_sum(vectors: list[vector]) -> vector:
    """sums all the corresponding elements"""
    # check that vectors is not empty
    assert vectors, "no vectors provided!"

    # check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i_th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

#3
# multiplying a vec by a scalar

def scalar_multiply(c: float, v: vector) -> vector:
    """multiplies every element by c"""
    return [c * v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

#4

def