from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 2 D8 From Die Class
d8_1 = Die(8)
d8_2 = Die(8)

# Rolling the 2 D8 Dices using for loop.
results = []
for roll_num in range(100_000):
    result = d8_1.roll() + d8_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = d8_1.num_sides + d8_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the Results.
x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

# Axes Configs
x_axis_config = {'title': 'Values', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

# Layout
my_layout = Layout(title='Results of rolling 2 D8 for 100000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)

# Offline Plot.
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
