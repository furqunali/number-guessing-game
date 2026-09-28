from number_guessing_core.leaderboard import LeaderboardEntry
from number_guessing_core.leaderboard_query import entries_for_player

def test_entries_for_player_filters_and_ranks():
    entries = [LeaderboardEntry("Alice", 100, 2), LeaderboardEntry("Alina", 300, 1), LeaderboardEntry("Bob", 200, 1)]
    assert [entry.player for entry in entries_for_player(entries, "ali")] == ["Alina", "Alice"]
