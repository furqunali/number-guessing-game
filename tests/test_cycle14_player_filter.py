from number_guessing_core.leaderboard import LeaderboardEntry, entries_for_player

def test_entries_for_player_is_case_insensitive():
    values = [LeaderboardEntry("Abi", 50, 2), LeaderboardEntry("Sam", 90, 1), LeaderboardEntry("ABI", 70, 3)]
    assert [e.score for e in entries_for_player(values, "abi")] == [70, 50]
