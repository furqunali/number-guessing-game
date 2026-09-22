"""Public API for the number-guessing domain package."""

from .engine import GuessEngine, GuessResult
from .feedback import feedback_distance, guess_feedback
from .history import GuessHistory, GuessRecord
from .leaderboard import LeaderboardEntry, rank_entries, validate_entry
from .limits import difficulty_for_limit, remaining_attempts, validate_attempt_limit
from .stats import GuessStats

__all__ = [
    "GuessEngine",
    "GuessResult",
    "GuessHistory",
    "GuessRecord",
    "LeaderboardEntry",
    "GuessStats",
    "difficulty_for_limit",
    "remaining_attempts",
    "validate_attempt_limit",
    "feedback_distance",
    "guess_feedback",
    "rank_entries",
    "validate_entry",
]
