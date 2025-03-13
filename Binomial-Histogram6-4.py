import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def bernoulli_trial(p: float) -> int:
    """returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    """returns the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))

from collections import Counter

def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """picks points from a binomial(n,p) and plots their histogram"""
    data = [binomial(n, p) for _ in range(num_points)]

    # bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

import matplotlib.pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs],'-', label='mu=0, sigma=1')

plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '-', label='mu=0, sigma=2')

plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')

plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-', label='mu=-1, sigma=1')

plt.legend(loc=4) #buttom right
plt.title("Various Normal cdfs")
plt.show()