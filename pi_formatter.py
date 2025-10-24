import numpy as np

def format_value(val, epsilon=2e-2):
    """
    Format a numerical value as a fraction of π if it's close to n*π/m.

    Args:
        val: numerical value to format
        epsilon: tolerance for matching (default 1e-9)

    Returns:
        String representation, either as a π fraction or decimal
    """
    if abs(val) < epsilon:
        return "0"

    # Check denominators in order of preference (simpler fractions first)
    for m in [1, 2, 4, 8]:
        for n in range(-16, 17):
            if n == 0:
                continue

            target = n * np.pi / m
            if abs(val - target) < epsilon:
                # Simplify the fraction display
                if m == 1:
                    if n == 1:
                        return "π"
                    elif n == -1:
                        return "-π"
                    else:
                        return f"{n}π"
                else:
                    if n == 1:
                        return f"π/{m}"
                    elif n == -1:
                        return f"-π/{m}"
                    else:
                        return f"{n}π/{m}"

    # No match found, return decimal
    return f"{val:.4f}"

def format_trig(val, angle_rad, epsilon=1e-2):
    """
    Format a trig value symbolically if angle is a nice π fraction.

    Args:
        val: numerical value (sin or cos of angle)
        angle_rad: the angle in radians
        epsilon: tolerance for matching

    Returns:
        Symbolic string like "sin(π/4)" or numerical fallback
    """
    angle_str = format_value(angle_rad, epsilon)

    # Only use symbolic form if angle is a π fraction (not decimal)
    if 'π' not in angle_str:
        return f"{val:.4f}"

    # Check if val matches cos(angle)
    if abs(val - np.cos(angle_rad)) < epsilon:
        return f"cos({angle_str})"

    # Check if val matches sin(angle)
    if abs(val - np.sin(angle_rad)) < epsilon:
        return f"sin({angle_str})"

    # Check if val matches -sin(angle)
    if abs(val + np.sin(angle_rad)) < epsilon:
        return f"-sin({angle_str})"

    # Check if val matches -cos(angle)
    if abs(val + np.cos(angle_rad)) < epsilon:
        return f"-cos({angle_str})"

    # Fallback to numerical
    return f"{val:.4f}"

def format_rotation_matrix(R, theta, epsilon=1e-2):
    """
    Format a 2D rotation matrix, using symbolic trig if theta is a π fraction.

    Args:
        R: 2x2 rotation matrix
        theta: rotation angle in radians
        epsilon: tolerance for matching

    Returns:
        Formatted string for matrix display
    """
    r00 = format_trig(R[0,0], theta, epsilon)
    r01 = format_trig(R[0,1], theta, epsilon)
    r10 = format_trig(R[1,0], theta, epsilon)
    r11 = format_trig(R[1,1], theta, epsilon)

    return f'R = [{r00:>12}  {r01:>12}]\n    [{r10:>12}  {r11:>12}]'
