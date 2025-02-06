from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 265]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# to show multiple series calls on the same chart/making multiple calls to plt.plot

plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b-', label='total error') # blue dotted line

plt.legend(loc=9) # loc=9 ---top center
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()