# 15-6. Two D8s: Create a simulation showing what happens when you roll two eight-sided dice 1000 times.
# Try to picture what you think the visualization will look like before you run the simulation;
# then see if your intuition was correct. Gradually increase the number of rolls until you start to see the
# limits of your system’s capabilities.

from plotly.graph_objs import Bar, Layout
from plotly import offline
from RollingDice import Die

# 8 sided die D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# We’ll analyze the results of rolling one D8 by counting how many times we roll each number:
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

# 15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18.
# Create a visualization that shows what happens when you roll three D6 dice.

# create 3 D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# We’ll analyze the results of rolling three D6 by counting how many times we roll each number:
frequencies = []
max_result = die_1.sides + die_2.sides + die_3.sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')

# 15-8. Multiplication: When you roll two dice, you usually add the two numbers together to get the result.
# Create a visualization that shows what happens if you multiply these numbers instead.

# create 2 D6 dice
die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# We’ll analyze the results of rolling two multiply D6 by counting how many times we roll each number:
frequencies = []
max_result = die_1.sides * die_2.sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two multiply D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6__d6.html')

# 15-9. Die Comprehensions: For clarity, the listings in this section use the long form of for loops.
# If you’re comfortable using list comprehensions, try writing a comprehension
# for one or both of the loops in each of these programs.

# create 2 D6 dice
die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list.
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)
# list Comprehension
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# We’ll analyze the results of rolling two D6 by counting how many times we roll each number:
# frequencies = []
max_result = die_1.sides + die_2.sides
# for value in range(1, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
# list Comprehension
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6___d6.html')

