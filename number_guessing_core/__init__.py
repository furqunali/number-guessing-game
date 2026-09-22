"""Public API for the number-guessing domain package."""

from .engine import GuessEngine, GuessResult
from .limits import difficulty_for_limit, remaining_attempts, validate_attempt_limit
from .stats import GuessStats

__all__ = [
    "GuessEngine",
    "GuessResult",
    "GuessStats",
    "difficulty_for_limit",
    "remaining_attempts",
    "validate_attempt_limit",
]

from .leaderboard import validate_entry
