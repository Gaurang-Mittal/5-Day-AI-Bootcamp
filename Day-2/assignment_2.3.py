import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 4 * np.pi, 200)

# Calculate sine values
y = np.sin(x)

# Plot the sine wave
plt.figure(figsize=(8, 4))

plt.plot(x, y, color="blue", linewidth=2, label="sin(x)")

# Add title and labels
plt.title("Sine Wave")
plt.xlabel("X (Radians)")
plt.ylabel("sin(x)")

# Add grid and legend
plt.grid(True)
plt.legend()

# Display the graph
plt.show()