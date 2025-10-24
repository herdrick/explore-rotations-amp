# elliptical_rotation_family.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pi_formatter import format_value

def R2(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s],[s, c]])

def M_theta_r(theta, r):
    # S = diag(r, 1) is equivalent to a/b = r
    # M = S^{-1} R S  -> explicit closed form avoids matrix mult & keeps it stable
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -r*s],[s/r, c]])

def ellipse_points(r, n=400):
    # Ellipse with semi-axes (a,b) = (r, 1). (Scaling overall doesn't matter.)
    t = np.linspace(0, 2*np.pi, n)
    return np.vstack((r*np.cos(t), np.sin(t)))

# --- initial params
theta0_deg = 30.0
phi0_deg   = 10.0
logr0      = 0.0   # log10(r); r=10**logr, so logr=0 -> r=1 (circle)

# --- figure
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.12, right=0.98, bottom=0.23, top=0.87)

# draw ellipse
r0 = 10.0**logr0
E = ellipse_points(r0)
(ell_line,) = ax.plot(E[0], E[1], lw=1.5, alpha=0.85, label='ellipse (a=r, b=1)')

def base_point(r, phi_rad):
    return np.array([r*np.cos(phi_rad), np.sin(phi_rad)])

# random points
np.random.seed(42)
n_pts = 100
random_pts = np.random.randn(2, n_pts) * 0.8
theta0 = np.deg2rad(theta0_deg)
transformed_pts = M_theta_r(theta0, r0) @ random_pts

(pt0_scatter,) = ax.plot(random_pts[0], random_pts[1], 'o', alpha=0.5, ms=4, label='random points')
(ptθ_scatter,) = ax.plot(transformed_pts[0], transformed_pts[1], 'o', alpha=0.5, ms=4, label='M(θ,r)·points')

ax.set_aspect('equal', adjustable='box')
ax.grid(True, alpha=0.35)
ax.legend(loc='upper right')

m = 1.4*max(r0, 1.0)
ax.set_xlim(-m, m); ax.set_ylim(-m, m)
ax.set_title("From circle → ellipse → line via aspect ratio r")

M0 = M_theta_r(theta0, r0)
matrix_text = fig.text(0.5, 0.94, '', ha='center', va='top', family='monospace', fontsize=10)
matrix_text.set_text(f'M = [{format_value(M0[0,0]):>10}  {format_value(M0[0,1]):>10}]\n    [{format_value(M0[1,0]):>10}  {format_value(M0[1,1]):>10}]')

# --- sliders
ax_theta = plt.axes([0.12, 0.16, 0.76, 0.03])
ax_phi   = plt.axes([0.12, 0.12, 0.76, 0.03])
ax_logr  = plt.axes([0.12, 0.08, 0.76, 0.03])

s_theta = Slider(ax_theta, 'θ', -180.0, 180.0, valinit=theta0_deg, valfmt='%1.1f°')
s_phi   = Slider(ax_phi,   'φ', -180.0, 180.0, valinit=phi0_deg, valfmt='%1.1f°')
# logr in [-3, +3] -> r in [1e-3, 1e+3]. Avoid exactly r=0.
s_logr  = Slider(ax_logr,  'shape: log₁₀ r', -3.0, 3.0, valinit=logr0)
s_theta.valtext.set_text(f'{theta0_deg:.1f}° = {format_value(np.deg2rad(theta0_deg))}')
s_phi.valtext.set_text(f'{phi0_deg:.1f}° = {format_value(np.deg2rad(phi0_deg))}')

ax_reset = plt.axes([0.12, 0.02, 0.15, 0.04])
btn_reset = Button(ax_reset, 'Reset')

def update(_):
    theta = np.deg2rad(s_theta.val)
    phi   = np.deg2rad(s_phi.val)
    logr  = s_logr.val
    r     = 10.0**logr

    # ellipse and points
    E = ellipse_points(r)
    ell_line.set_data(E[0], E[1])

    M = M_theta_r(theta, r)
    transformed_pts = M @ random_pts

    pt0_scatter.set_data(random_pts[0], random_pts[1])
    ptθ_scatter.set_data(transformed_pts[0], transformed_pts[1])

    # autoscale with r
    m = 1.4*max(r, 1.0)
    ax.set_xlim(-m, m); ax.set_ylim(-m, m)

    matrix_text.set_text(f'M = [{format_value(M[0,0]):>10}  {format_value(M[0,1]):>10}]\n    [{format_value(M[1,0]):>10}  {format_value(M[1,1]):>10}]')
    s_theta.valtext.set_text(f'{s_theta.val:.1f}° = {format_value(theta)}')
    s_phi.valtext.set_text(f'{s_phi.val:.1f}° = {format_value(phi)}')

    fig.canvas.draw_idle()

def reset(_):
    s_theta.reset()
    s_phi.reset()
    s_logr.reset()

for s in (s_theta, s_phi, s_logr):
    s.on_changed(update)

btn_reset.on_clicked(reset)
plt.show()
