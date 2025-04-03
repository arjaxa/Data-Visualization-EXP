from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt

def bucketize(point: float, bucket_size: float) -> float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: list[float], bucket_size: float) -> dict[float, int]:
    """buckets the points and counts how many in each bucket"""
    return Counter(bucket_size(point, bucket_size) for point in points)

