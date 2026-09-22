from number_guessing_core.leaderboard import LeaderboardEntry, top_entries

def test_top_entries_limits_ranked_results():
    entries = [LeaderboardEntry("A", 100, 2), LeaderboardEntry("B", 300, 3), LeaderboardEntry("C", 200, 1)]
    assert [entry.player for entry in top_entries(entries, 2)] == ["B", "C"]
