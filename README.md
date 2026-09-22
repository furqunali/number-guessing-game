# 🔢 Number Guessing Game

A small interactive **command-line number-guessing game** in Python, designed as a training project for input validation, game state, scoring, and testing.

## Install

Requires Python 3.11+.

```bash
python -m pip install -e ".[dev]"
```

## Run

```bash
python app.py
```

## Test

```bash
pytest
```

## What it shows

- Integer input and attempt-limit validation
- Deterministic game-engine behavior
- Scoring and guess statistics
- Testable domain logic separated from the CLI
- Stable public API through `number_guessing_core`

## Structure

- `number_guessing_core/` — reusable game domain
- `app.py` — command-line entry point
- `tests/` — automated tests
