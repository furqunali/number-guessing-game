"""Public API for the number-guessing domain package."""

from .engine import GuessEngine, GuessResult
from .feedback import feedback_distance, guess_feedback
from .history import GuessHistory, GuessRecord, history_from_json, history_to_json
from .leaderboard import LeaderboardEntry, leaderboard_from_dict, leaderboard_to_dict, rank_entries, top_entries, validate_entry
from .limits import difficulty_for_limit, remaining_attempts, validate_attempt_limit
from .stats import GuessStats

__all__ = [
    "GuessEngine",
    "GuessResult",
    "GuessHistory",
    "GuessRecord",
    "history_to_json",
    "history_from_json",
    "LeaderboardEntry",
    "GuessStats",
    "difficulty_for_limit",
    "remaining_attempts",
    "validate_attempt_limit",
    "feedback_distance",
    "guess_feedback",
    "rank_entries",
    "top_entries",
    "validate_entry",
    "leaderboard_to_dict",
    "leaderboard_from_dict",
]
