import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pyparsing import line

# setup the figure and axis,line object

fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 200)
line, = ax.plot(x, np.sin(x), color='green', lw=2)

line.set_ydata(np.cos(x))
display(fig)

from matplotlib.animation import FuncAnimation
from IPython.display import HTML

x = np.linspace(0, 2*np.pi, 200)
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x), lw=3)
ax.set_ylim(-1.2, 1.2)

def update(phase):
    line.set_ydata(np.sin(x + phase))
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, np.pi/2, 60),
                    interval=40, blit=True)

HTML(ani.to_jshtml())