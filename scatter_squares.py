import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set Chart Title and label axes.
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('square of values', fontsize=14)

# Set size of tick label
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
