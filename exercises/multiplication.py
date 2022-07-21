# 1.Importing Required Modules
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 2.Instantation
d6_1 = Die(6)
d6_2 = Die(6)

# 3.applying the Objects behaviour
results = []
for roll_num in range(1000):
    result = d6_1.roll() * d6_2.roll()
    results.append(result)

# 4.Analyze the Object's behaviour
frequencies = []
max_result = d6_1.num_sides + d6_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 5.Visualize the results Analyzation.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

#5.1Configure the Axes.
x_axis_config = {'title': "Results", 'dtick': 1}
y_axis_config = {'title': 'frequency of results'}

#5.2Layout
my_layout = Layout(title='result of rolling two D6s 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)

#6 offline plot
offline.plot({'data': data, 'layout': my_layout}, filename='d6_Multi.html')
