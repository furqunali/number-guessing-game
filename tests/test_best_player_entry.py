from number_guessing_core.leaderboard import LeaderboardEntry, best_entry_for_player

def test_best_entry_for_player_returns_highest_ranked_record():
    entries = [LeaderboardEntry("Mina", 300, 2), LeaderboardEntry("mina", 600, 3)]
    assert best_entry_for_player(entries, "MINA").score == 600

def test_best_entry_for_unknown_player_is_none():
    assert best_entry_for_player([], "nobody") is None
