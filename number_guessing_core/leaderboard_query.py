from collections.abc import Iterable
from .leaderboard import LeaderboardEntry, rank_entries

def entries_for_player(entries: Iterable[LeaderboardEntry], player: str) -> list[LeaderboardEntry]:
    """Return ranked leaderboard entries for a case-insensitive player name."""
    needle = str(player).strip().casefold()
    if not needle:
        return []
    matches = [entry for entry in entries if needle in entry.player.casefold()]
    return rank_entries(matches)
