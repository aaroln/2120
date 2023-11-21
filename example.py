import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 7, 12, 9]

# Create a line plot
plot = plt.plot(x_values, y_values, marker='o')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Plot')

# Display the plot
plt.show()