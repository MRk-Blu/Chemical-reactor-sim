# Chemical Reactor Simulation

An OOP-based Python learning project for modeling chemical storage and reactor
operations. The examples explore tank capacity, adding and draining material,
Newton's-law temperature change, heating and cooling, and basic safety limits.

## Requirements

- Python 3.10 or newer
- SciPy for the more complete reactor examples
- NumPy for the array exercises

Create an environment and install the optional dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy scipy
```

The small tank example only uses the Python standard library, so it can also
run without installing NumPy or SciPy.

## Running the Examples

Run commands from the repository root. The files are standalone experiments,
so choose an example based on what you want to study:

```powershell
python Reactor_8.py
python Reactor_1.py
python "Chemical Plant.py"
python "CHEMICAL TANK_2.py"
python "numpy main.py"
```

`Reactor_8.py` is the most complete interactive example in the current set. It
asks for a mode, chemical name, temperatures, heat-transfer constant, amount,
limits, density, and run time. Its modes are:

1. Add material
2. Drain material
3. Heat the reactor
4. Cool the reactor

Several operations call `time.sleep(1)`, so a long run intentionally takes real
time. Use a short run time while experimenting.

## Repository Layout

- `Reactor_1.py` through `Reactor_10.py`: incremental reactor experiments
- `CHEMICAL TANK_*.py`: tank-focused exercises
- `Chemical Plant.py`: chemical plant exercise
- `numpy main.py` and `numpy tests/`: NumPy exercises
- `Raactor_array/`: array-based reactor experiments
- `pathlib.md`: notes on Python `pathlib`
- `run_*/`: saved reactor output logs from previous runs

## Logs

The existing `run_*/` folders contain saved `Reactor Log.txt` files and are
kept visible to Git intentionally. In the current `Reactor_8.py` code, new
logs are written to `C:\\BLU\\DOCS` rather than automatically to this
repository. Change `log_dir` near the top of that file if logs should be saved
elsewhere.

## Project Status

This is a collection of progressively expanded practice scripts, not a
published Python package. The scripts still contain exploratory code and are
run directly; there is no automated test suite or shared command-line
interface yet.

## License

This project is licensed under the [MIT License](LICENSE).
