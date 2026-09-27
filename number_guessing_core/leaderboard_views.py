from collections.abc import Iterable
from .leaderboard import LeaderboardEntry, validate_entry

def filter_score_band(entries: Iterable[LeaderboardEntry], minimum: int, maximum: int | None = None) -> list[LeaderboardEntry]:
    """Select validated leaderboard entries within an inclusive score band."""
    if isinstance(minimum, bool) or not isinstance(minimum, int) or minimum < 0:
        raise ValueError("minimum must be a non-negative integer")
    if maximum is not None and (isinstance(maximum, bool) or not isinstance(maximum, int) or maximum < minimum):
        raise ValueError("maximum must be an integer at least minimum")
    selected = [validate_entry(entry) for entry in entries if entry.score >= minimum and (maximum is None or entry.score <= maximum)]
    return sorted(selected, key=lambda entry: (-entry.score, entry.attempts, entry.player.casefold()))
