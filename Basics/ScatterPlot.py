import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# set chart title and label axis
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square value', fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
# If you want to disable both the offset and scientific notation.
ax.ticklabel_format(useOffset=False, style='plain')

# set range of each axis
ax.axis([0, 1100, 0, 1100000])
plt.tight_layout()

plt.show()
