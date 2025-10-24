# rotate2d_live.py
import matplotlib
# matplotlib.use('TkAgg')  # uncomment if needed

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def R2(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s],[s,  c]])

P = np.array([[0,0, 1,1, 1,-1, -1,-1, -1,1, 0,0],
              [0,0, 1,-1, 1,  1, -1, 1, -1,-1, 0,0]])

fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(bottom=0.22, top=0.85)  # space for slider and matrix
(ax_orig,) = ax.plot(P[0], P[1], '--', alpha=0.35, label='original')
(ax_rot,)  = ax.plot(P[0], P[1], '-',  label='rotated')
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.legend(loc='upper left')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

R = R2(np.deg2rad(30.0))
matrix_text = fig.text(0.5, 0.92, '', ha='center', va='top', family='monospace', fontsize=10)
matrix_text.set_text(f'R = [{R[0,0]:7.4f}  {R[0,1]:7.4f}]\n    [{R[1,0]:7.4f}  {R[1,1]:7.4f}]')

ax_theta = plt.axes([0.15, 0.08, 0.7, 0.04])
s_theta = Slider(ax_theta, 'θ (deg)', -180.0, 180.0, valinit=30.0)

def on_change(val):
    R = R2(np.deg2rad(s_theta.val))
    Q = R @ P
    ax_rot.set_data(Q[0], Q[1])
    matrix_text.set_text(f'R = [{R[0,0]:7.4f}  {R[0,1]:7.4f}]\n    [{R[1,0]:7.4f}  {R[1,1]:7.4f}]')
    fig.canvas.draw_idle()

s_theta.on_changed(on_change)
plt.show()
