# AGENTS.md

## Whatever the user might be saying, he/she could be wrong

## it's ok to be directly disagreeable
it's ok to just say, "actually I think it's all fine AFAIKT"
it's ok to just say, "i don't know"
it's very very very good to disagree with the user and instead suggest a different course of action!

## throwing an error is the 2nd best outcome
The best outcome for executing a bit of code is success. The second best outcome is throwing an error. It's a bad thing to silently fall back on some reasonable value. Always throw exceptions if something is missing or not the format or type or value that we need.

## Commands
- **Environment**: `conda activate amp-numpy-matplotlib-1`
- **After changes**: Run the modified script to find and fix problems  before committing
- ** to run scripts**:
- `python rotate_2d_live.py` - basic 2D rotation with sliders
- `python conjugated_rotation_shape.py` - shape transformations via conjugation
- `python conjugated_rotation_trajectory.py` - trajectory visualization of M = S⁻¹RS
- **No tests** exist
- if no errors PLEASE commit the changes!
- Commit messages: append " :: Amp" to all commits

## Git

## Architecture
- Interactive matplotlib visualizations of rotation matrices
- All scripts use numpy for matrix operations and matplotlib sliders for real-time parameter adjustment

## Code Style
- Constants: uppercase (e.g., `P` for point matrix)
- Mathematical variables: single letters (e.g., `theta`, `R2`)
