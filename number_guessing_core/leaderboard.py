from dataclasses import dataclass

@dataclass(frozen=True)
class LeaderboardEntry:
    player: str
    score: int
    attempts: int

def validate_entry(entry: LeaderboardEntry) -> LeaderboardEntry:
    if not isinstance(entry, LeaderboardEntry):
        raise TypeError("entry must be a LeaderboardEntry")
    player = entry.player.strip()
    if not player:
        raise ValueError("player name is required")
    if isinstance(entry.score, bool) or not isinstance(entry.score, int) or entry.score < 0:
        raise ValueError("score must be a non-negative integer")
    if isinstance(entry.attempts, bool) or not isinstance(entry.attempts, int) or entry.attempts < 1:
        raise ValueError("attempts must be a positive integer")
    return LeaderboardEntry(player, entry.score, entry.attempts)

def rank_entries(entries: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
    """Rank by score, attempts, then case-insensitive player name."""
    values = [validate_entry(entry) for entry in entries]
    return sorted(values, key=lambda e: (-e.score, e.attempts, e.player.casefold(), e.player))

def top_entries(entries: list[LeaderboardEntry], limit: int = 10) -> list[LeaderboardEntry]:
    """Return a bounded leaderboard without mutating the supplied entries."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 1:
        raise ValueError("limit must be positive")
    return rank_entries(entries)[:limit]

def tied_entries(entries: list[LeaderboardEntry]) -> dict[tuple[int, int], list[LeaderboardEntry]]:
    """Group entries sharing the same score and attempt count."""
    groups: dict[tuple[int, int], list[LeaderboardEntry]] = {}
    for entry in rank_entries(entries):
        groups.setdefault((entry.score, entry.attempts), []).append(entry)
    return {key: group for key, group in groups.items() if len(group) > 1}
