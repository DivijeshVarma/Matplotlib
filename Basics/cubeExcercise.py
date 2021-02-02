# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and
# then plot the first 5000 cubic numbers. 15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [x**3 for x in x_values]

x_values = list(range(5000))
cubes = [x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Greens, s=10)

ax.set_title('cubic numbers', fontsize=24)
ax.set_xlabel('Number', fontsize=14)
ax.set_ylabel('Cubes', fontsize=14)

# set size of tick labels and set range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100 ** 3])
# If you want to disable both the offset and scientific notation.
ax.ticklabel_format(useOffset=False, style='plain')

plt.tight_layout()

plt.show()
