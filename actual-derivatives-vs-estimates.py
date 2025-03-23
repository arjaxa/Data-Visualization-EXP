from typing import Callable
import matplotlib.pyplot as plt

def difference_qoutient(f: callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

def derivative(x: float) -> float:
    return 2 * x

xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_qoutient(square, x, h=0.001) for x in xs]

plt.title("Actual Derivatives vs. Estimates")
plt.plot(xs, actuals, 'rx', label='Actual') #red x
plt.plot(xs, estimates, 'b+', label='Estimates') #blue +
plt.legend(loc=9)
plt.show()