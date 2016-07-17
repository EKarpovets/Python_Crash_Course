import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=3)
# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


plt.show()