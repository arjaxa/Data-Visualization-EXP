from matplotlib import pyplot as plt

movies = ["John wick", "Togo", "Arcane", "8 Bellow", "Inception"]
num_oscars = [5, 11, 3, 8, 10]

# plot bar with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

# x-axis label with movie names at bar centers
plt.xticks(range(len(movies)), movies)

plt.show()