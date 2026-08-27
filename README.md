# Chemical Reactor Simulator Remodeled

A remodification of the former Chemical Reactor Simulator. The long-term goal is to advance the original reactor-focused project into a small factory simulation, with connected storage, processing stages, material flow, and eventually larger production systems. Development has only just started in this repository, so the current code is an early foundation rather than a complete factory simulator.

## Current Features

- `ChemicalTank` models a named liquid tank with a current amount, maximum capacity, and temperature.
- `ChemicalTank.add_liquid()` simulates timed liquid addition and reports the amount in the tank.
- `Parameter_Store_house.py` contains early numeric-input and NumPy-array experiments.
- `CodeTester.ipynb` provides an interactive place to test the project.

## Planned Direction

The project is intended to grow from a single-reactor model into a more complete factory simulation. Possible future systems include multiple connected tanks, pumps and transfer rates, reactor recipes, input and output materials, temperature and safety controls, production timing, and factory-wide resource management.

## Project Layout

| File | Purpose |
| --- | --- |
| `Reactormod_1.py` | Early reactor module entry point |
| `Referencer.py` | `ChemicalTank` class and timed liquid-addition example |
| `Parameter_Store_house.py` | Numeric conversion and array-building experiments |
| `CodeTester.ipynb` | Interactive experiments and checks |
| `issues.md` | Known issues and development notes |
| `dummy.py` | Scratch code for future array-input work |

## Requirements

- Python 3.10 or newer
- NumPy
- Jupyter, if you want to use the notebook

## Setup

Create and activate a virtual environment, then install the runtime dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy jupyter
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Running the Examples

From the project root:

```powershell
python Referencer.py
python Parameter_Store_house.py
```

To open the notebook:

```powershell
jupyter notebook CodeTester.ipynb
```

A basic use of the tank class looks like this:

```python
from Referencer import ChemicalTank

tank = ChemicalTank("HCl", Current_gallons=100, max_capacity=1000)
print(tank.add_liquid(rate=3, Time_to_add=20))
```

`add_liquid()` currently waits in real time, so the example takes approximately 20 seconds to complete.

## Development Notes

This repository is at the beginning of that transition. The existing files are exploratory work inherited from the reactor-simulation concept, and many of the factory-simulation systems have not been implemented yet. Input validation, capacity enforcement, naming consistency, test coverage, and separation of demonstration code from importable modules are still being developed. See [`issues.md`](issues.md) for the current issue notes.

Generated files, virtual environments, and local editor settings are excluded by [`.gitignore`](.gitignore). Please keep source files, notebooks, and documentation under version control when they are part of an experiment or feature.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for the full text.
