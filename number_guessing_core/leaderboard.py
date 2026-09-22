from dataclasses import dataclass

@dataclass(frozen=True)
class LeaderboardEntry:
    player: str
    score: int
    attempts: int

def rank_entries(entries: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
    return sorted(entries, key=lambda e: (-e.score, e.attempts, e.player.lower()))
