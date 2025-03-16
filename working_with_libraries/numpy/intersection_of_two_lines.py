import numpy as np
import matplotlib.pyplot as plt


def line_intersection(line1, line2):
    intersection = np.cross(line1, line2)
    if intersection[2] != 0:
        intersection = intersection / intersection[2]
    return intersection


def plot_line(line, x_range, label):
    a, b, c = line
    if b != 0:
        y = (-a * x_range - c) / b
        plt.plot(x_range, y, label=label)
    else:
        x = -c / a
        plt.axvline(x=x, label=label)


# Example lines: line1: 2x + 3y + 6 = 0, line2: x - 4y + 5 = 0
line1 = [2, 3, 6]
line2 = [1, -4, 5]

# Calculate intersection
intersect = line_intersection(line1, line2)
print("Intersection Point (Homogeneous Coordinates):", intersect)

# Plotting
x_range = np.linspace(-10, 10, 400)
plot_line(line1, x_range, label="2x + 3y + 6 = 0")
plot_line(line2, x_range, label="x - 4y + 5 = 0")

# Plot intersection point
plt.scatter(intersect[0], intersect[1], color="red", label="Intersection")

# Add labels and legend
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title("Intersection of Two Lines")
plt.show()
