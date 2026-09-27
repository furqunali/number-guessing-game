from number_guessing_core.leaderboard import LeaderboardEntry, entries_for_player

def test_entries_for_player_matches_case_insensitively():
    entries = [LeaderboardEntry("Abi", 90, 2), LeaderboardEntry("Sam", 80, 3), LeaderboardEntry("ABI", 70, 4)]
    assert [e.score for e in entries_for_player(entries, "abi")] == [90, 70]
