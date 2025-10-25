import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Base circle
t = np.linspace(0, 2*np.pi, 400)
r = 1
circle = np.vstack((r*np.cos(t), r*np.sin(t)))  # shape (2, N)

# Set up figure and axes
fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(bottom=0.25)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)

# Plot circle and projected ellipse
(circle_line,) = ax.plot(circle[0], circle[1], '--', label='circle')
(ellipse_line,) = ax.plot([], [], '-', label='viewed ellipse')
ax.legend()

# Slider for tilt angle θ (degrees)
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Tilt θ (deg)', 0, 360, valinit=0)

def update(val):
    theta = np.deg2rad(slider.val)
    a, b = 1, np.cos(theta)  # squash vertical axis by cos(θ)
    T = np.array([[a, 0],
                  [0, b]])
    ellipse = T @ circle
    ellipse_line.set_data(ellipse[0], ellipse[1])
    fig.canvas.draw_idle()

slider.on_changed(update)
update(0)
plt.show()
