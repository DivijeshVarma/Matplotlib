from RollingDice import Die

# 6 sided die D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50):
    result = die.roll()
    results.append(result)

print(results)