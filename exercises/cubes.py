import matplotlib.pyplot as plt

# Define Data Set.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

# Make Plot.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set Chart title and labels axes.
ax.set_title("Cube Values", fontsize=24)
ax.set_xlabel("Values", fontsize=16)
ax.set_ylabel("Cube of Values", fontsize=16)

# Customize the labels and set range for axis.
ax.tick_params(axis='both', labelsize=16)
ax.axis([0, 6, 0, 130])

# Show Plot
plt.show()
