from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990,  2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# creating a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# title
plt.title("Nominal GDP")

# y-axis label
plt.ylabel("Billions of $")
plt.show()
