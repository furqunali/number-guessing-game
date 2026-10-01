# 🔢 Number Guessing Game

A small interactive **command-line number-guessing game** in Python, designed as a training project for input validation, game state, scoring, persistence, and testing.

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
- JSON persistence for guess history and leaderboard snapshots
- Stable public API through `number_guessing_core`

## Public API

The reusable package exposes:

- `GuessEngine` / `GuessResult` — deterministic game state
- `GuessHistory` — validated attempt history
- `GuessStats` — scoring and attempt analytics
- `LeaderboardEntry` and ranking helpers
- `history_to_json` / `history_from_json`
- `leaderboard_to_dict` / `leaderboard_from_dict`

## Persistence

Guess history can be serialized to JSON and restored with the same validation rules as normal domain construction.

```python
from number_guessing_core import history_from_json, history_to_json

payload = history_to_json(history)
restored = history_from_json(payload)
```

## Structure

- `number_guessing_core/` — reusable game domain
- `app.py` — command-line entry point
- `tests/` — automated tests

## Roadmap

- CLI leaderboard presentation
- Exportable session reports
- Difficulty presets
- Small API/demo surface for the reusable engine
