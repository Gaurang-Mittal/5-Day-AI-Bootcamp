import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 500)

# Create a damped sine wave
amplitude = np.exp(-0.3 * time) * np.sin(2 * np.pi * time)

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)

# Plot the data
ax.plot(
    time,
    amplitude,
    color='green',
    linewidth=2,
    label='Sensor A displacement'
)

# Customize the graph
ax.set_title(
    'Damped Harmonic Response of Structure',
    fontsize=14,
    fontweight='bold',
    pad=15
)

ax.set_xlabel('Time (seconds)', fontsize=12)
ax.set_ylabel('Displacement (mm)', fontsize=12)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper right', frameon=True, shadow=True)

# Display graph
plt.show() 