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
    values = [validate_entry(entry) for entry in entries]
    return sorted(values, key=lambda e: (-e.score, e.attempts, e.player.casefold(), e.player))

def top_entries(entries: list[LeaderboardEntry], limit: int = 10) -> list[LeaderboardEntry]:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 1:
        raise ValueError("limit must be positive")
    return rank_entries(entries)[:limit]

def tied_entries(entries: list[LeaderboardEntry]) -> dict[tuple[int, int], list[LeaderboardEntry]]:
    groups: dict[tuple[int, int], list[LeaderboardEntry]] = {}
    for entry in rank_entries(entries):
        groups.setdefault((entry.score, entry.attempts), []).append(entry)
    return {key: group for key, group in groups.items() if len(group) > 1}

def entries_for_player(entries: list[LeaderboardEntry], player: str) -> list[LeaderboardEntry]:
    name = str(player).strip().casefold()
    if not name:
        return []
    return [entry for entry in rank_entries(entries) if entry.player.casefold() == name]

def best_entry_for_player(entries: list[LeaderboardEntry], player: str) -> LeaderboardEntry | None:
    """Return the highest-ranked record for a player, or None when absent."""
    matches = entries_for_player(entries, player)
    return matches[0] if matches else None


def leaderboard_to_dict(entries: list[LeaderboardEntry]) -> dict[str, list[dict[str, int | str]]]:
    """Return a JSON-compatible snapshot of validated leaderboard entries."""
    return {
        "entries": [
            {
                "player": entry.player,
                "score": entry.score,
                "attempts": entry.attempts,
            }
            for entry in rank_entries(entries)
        ]
    }


def leaderboard_from_dict(data: dict) -> list[LeaderboardEntry]:
    """Restore and validate leaderboard entries from a snapshot."""
    if not isinstance(data, dict):
        raise TypeError("leaderboard snapshot must be a dictionary")
    values = data.get("entries")
    if not isinstance(values, list):
        raise ValueError("leaderboard snapshot entries must be a list")

    entries: list[LeaderboardEntry] = []
    for item in values:
        if not isinstance(item, dict):
            raise ValueError("leaderboard snapshot entries must contain dictionaries")
        try:
            entry = LeaderboardEntry(
                player=item["player"],
                score=item["score"],
                attempts=item["attempts"],
            )
        except KeyError as exc:
            raise ValueError(f"leaderboard entry is missing {exc.args[0]}") from exc
        entries.append(validate_entry(entry))
    return entries
