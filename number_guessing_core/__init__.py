"""Public API for the number-guessing domain package."""

from .engine import GuessEngine, GuessResult
from .limits import difficulty_for_limit, remaining_attempts, validate_attempt_limit
from .scoring import calculate_score
from .stats import GuessStats

__all__ = [
    "GuessEngine",
    "GuessResult",
    "GuessStats",
    "calculate_score",
    "difficulty_for_limit",
    "remaining_attempts",
    "validate_attempt_limit",
]
