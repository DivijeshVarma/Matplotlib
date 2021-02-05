import matplotlib.pyplot as plt
import numpy as np
from RollingDiceMatplot import Die

# create two D6 dice
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results.
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

plt.hist(results, bins=np.arange(2, max_result + 2) - .5, histtype='bar',
         rwidth=0.8, facecolor='blue', edgecolor="k")

plt.title("Dice Plot")
plt.xlabel("Results")
plt.ylabel("Frequency of Result")
plt.xticks(np.arange(2, max_result + 2))
plt.tight_layout()
bins = np.arange(1, max_result + 2) - .5
print(bins)
plt.show()
