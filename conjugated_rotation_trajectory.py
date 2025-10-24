# elliptical_rotation_live.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- math helpers -------------------------------------------------------------
def R2(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s],
                     [s,  c]])

def elliptical_rotation(a, b, theta):
    S = np.array([[a, 0.0],
                  [0.0, b]])
    Sinv = np.array([[1.0/a, 0.0],
                     [0.0,   1.0/b]])
    return Sinv @ R2(theta) @ S

def ellipse_points(a, b, n=400):
    t = np.linspace(0, 2*np.pi, n)
    return np.vstack((a*np.cos(t), b*np.sin(t)))

# --- initial params -----------------------------------------------------------
a0, b0 = 2.0, 1.2
theta0_deg = 30.0
phi0_deg = 10.0

# --- figure & axes ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.12, right=0.98, bottom=0.27, top=0.82)  # space for sliders and matrix

# base point on ellipse chosen by φ
def base_point(a, b, phi_rad):
    return np.array([a*np.cos(phi_rad), b*np.sin(phi_rad)])

# trajectory that p0 traces as θ varies
def trajectory_points(a, b, phi_rad, n=400):
    theta_vals = np.linspace(0, 2*np.pi, n)
    p0 = base_point(a, b, phi_rad)
    path = np.array([elliptical_rotation(a, b, t) @ p0 for t in theta_vals]).T
    return path

# ellipse outline (source space)
E = ellipse_points(a0, b0)
(ell_line,) = ax.plot(E[0], E[1], lw=1.5, alpha=0.4, ls='--', label='source ellipse')

# trajectory
traj = trajectory_points(a0, b0, np.deg2rad(phi0_deg))
(traj_line,) = ax.plot(traj[0], traj[1], lw=1.5, alpha=0.8, label='rotation trajectory')

# random points
np.random.seed(42)
n_pts = 100
random_pts = np.random.randn(2, n_pts) * 0.8  # spread around origin
M0 = elliptical_rotation(a0, b0, np.deg2rad(theta0_deg))
transformed_pts = M0 @ random_pts

(pt0_scatter,) = ax.plot(random_pts[0], random_pts[1], 'o', alpha=0.5, ms=4, label='random points')
(ptθ_scatter,) = ax.plot(transformed_pts[0], transformed_pts[1], 'o', alpha=0.5, ms=4, label='M(θ)·points')



# format the main axes
ax.set_aspect('equal', adjustable='box')
ax.grid(True, alpha=0.35)
ax.legend(loc='upper right')
ax.set_xlim(-max(a0,b0)*1.4, max(a0,b0)*1.4)
ax.set_ylim(-max(a0,b0)*1.4, max(a0,b0)*1.4)
ax.set_title("Elliptical 'Rotation'  M(θ) = S⁻¹ R(θ) S")

# matrix display text
M0 = elliptical_rotation(a0, b0, np.deg2rad(theta0_deg))
matrix_text = fig.text(0.5, 0.92, '', ha='center', va='top', family='monospace', fontsize=10)
matrix_text.set_text(f'M = [{M0[0,0]:7.4f}  {M0[0,1]:7.4f}]\n    [{M0[1,0]:7.4f}  {M0[1,1]:7.4f}]')

# --- sliders ------------------------------------------------------------------
# regions: [left, bottom, width, height] in figure fraction coords
ax_theta = plt.axes([0.12, 0.19, 0.76, 0.03])
ax_phi   = plt.axes([0.12, 0.15, 0.76, 0.03])
ax_a     = plt.axes([0.12, 0.11, 0.76, 0.03])
ax_b     = plt.axes([0.12, 0.07, 0.76, 0.03])

s_theta = Slider(ax_theta, 'θ (deg)', -180.0, 180.0, valinit=theta0_deg)
s_phi   = Slider(ax_phi,   'φ (deg)', -180.0, 180.0, valinit=phi0_deg)
s_a     = Slider(ax_a,     'a (x-axis)', 0.3, 4.0, valinit=a0)
s_b     = Slider(ax_b,     'b (y-axis)', 0.3, 4.0, valinit=b0)

# --- update callback ----------------------------------------------------------
def update(_):
    a = s_a.val
    b = s_b.val
    theta = np.deg2rad(s_theta.val)
    phi   = np.deg2rad(s_phi.val)

    # update ellipse outline
    E = ellipse_points(a, b)
    ell_line.set_data(E[0], E[1])

    # update trajectory
    traj = trajectory_points(a, b, phi)
    traj_line.set_data(traj[0], traj[1])

    # transform random points
    M = elliptical_rotation(a, b, theta)
    transformed_pts = M @ random_pts

    pt0_scatter.set_data(random_pts[0], random_pts[1])
    ptθ_scatter.set_data(transformed_pts[0], transformed_pts[1])

    # autoscale a bit when a/b change
    m = 1.4*max(a, b)
    ax.set_xlim(-m, m)
    ax.set_ylim(-m, m)

    # update matrix display
    matrix_text.set_text(f'M = [{M[0,0]:7.4f}  {M[0,1]:7.4f}]\n    [{M[1,0]:7.4f}  {M[1,1]:7.4f}]')

    fig.canvas.draw_idle()

for slider in (s_theta, s_phi, s_a, s_b):
    slider.on_changed(update)

plt.show()
