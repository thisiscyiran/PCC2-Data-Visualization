from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 3 instance of Die with 6 sides
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# roll the all 3 D6s
results = []
for value in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = []
for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

# x and y values
x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

# config x and y axes
x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

# setup Layout
my_layout = Layout(title='results of rolling 3 D6s 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)

# Offline Plot
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')

