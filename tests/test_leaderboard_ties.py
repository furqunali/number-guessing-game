from number_guessing_core.leaderboard import LeaderboardEntry, tied_entries

def test_tied_entries_groups_same_score_and_attempts():
    entries = [LeaderboardEntry("Ali", 500, 3), LeaderboardEntry("Bea", 500, 3), LeaderboardEntry("Cy", 400, 2)]
    assert [entry.player for entry in tied_entries(entries)[(500, 3)]] == ["Ali", "Bea"]
