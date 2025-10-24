# AGENTS.md

## Commands
- **Environment**: `conda activate amp-numpy-matplotlib-1`
- **Run scripts**: 
  - `python rotate_2d_live.py` - basic 2D rotation with sliders
  - `python conjugated_rotation_shape.py` - shape transformations via conjugation
  - `python conjugated_rotation_trajectory.py` - trajectory visualization of M = S⁻¹RS
- **After changes**: Run the modified script to verify correctness before committing
- **No tests** exist

## Architecture
- Interactive matplotlib visualizations of rotation matrices
- All scripts use numpy for matrix operations and matplotlib sliders for real-time parameter adjustment

## Code Style
- Constants: uppercase (e.g., `P` for point matrix)
- Mathematical variables: single letters (e.g., `theta`, `R2`)

## Git
- Commit messages: append " :: Amp" to all commits