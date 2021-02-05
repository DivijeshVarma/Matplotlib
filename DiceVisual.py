from RollingDice import Die

# 6 sided die D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# We’ll analyze the results of rolling one D6 by counting how many times we roll each number:
frequencies = []
for value in range(1, die.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

