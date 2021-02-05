from plotly.graph_objs import Bar, Layout
from plotly import offline
from RollingDice import Die

# create 2 D6 dice
die_1 = Die()
# die_2 = Die()
# Rolling Dice of Different Sizes D10
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# We’ll analyze the results of rolling one D6 by counting how many times we roll each number:
frequencies = []
max_results = die_1.sides + die_2.sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_results + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 and D10 10_000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
