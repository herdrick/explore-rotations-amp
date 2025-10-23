# AGENTS.md

## Commands
- **Environment**: `conda activate amp-numpy-matplotlib-1`
- **Run script**: `python rotate_2d_live.py` or `python elliptical_rotation_live.py`
- **No tests** currently exist in this repository

## Architecture
- Python scripts for visualizing 2D rotations and elliptical rotations
- Uses matplotlib with interactive sliders to demonstrate rotation matrices
- `elliptical_rotation_live.py` shows M = S⁻¹RS transformations with trajectory visualization

## Code Style
- Python 3 with numpy and matplotlib dependencies
- Constants: uppercase (e.g., `P` for point matrix)
- Mathematical variables: single letters following convention (e.g., `theta`, `R2`)
- Matplotlib backend defaults to standard, TkAgg commented out if needed

## git
- if you do a commit, append " :: <your name>" where <your name> is the name of you, the agent