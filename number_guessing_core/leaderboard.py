from dataclasses import dataclass

@dataclass(frozen=True)
class LeaderboardEntry:
    player: str
    score: int
    attempts: int

def validate_entry(entry: LeaderboardEntry) -> LeaderboardEntry:
    if not isinstance(entry, LeaderboardEntry): raise TypeError("entry must be a LeaderboardEntry")
    player = entry.player.strip()
    if not player: raise ValueError("player name is required")
    if isinstance(entry.score, bool) or not isinstance(entry.score, int) or entry.score < 0: raise ValueError("score must be a non-negative integer")
    if isinstance(entry.attempts, bool) or not isinstance(entry.attempts, int) or entry.attempts < 1: raise ValueError("attempts must be a positive integer")
    return LeaderboardEntry(player, entry.score, entry.attempts)

def rank_entries(entries: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
    """Validate and deterministically rank entries by score, attempts, then name."""
    values = [validate_entry(entry) for entry in entries]
    return sorted(values, key=lambda e: (-e.score, e.attempts, e.player.casefold()))
