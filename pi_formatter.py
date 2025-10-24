import numpy as np

def format_value(val, epsilon=1e-2):
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
