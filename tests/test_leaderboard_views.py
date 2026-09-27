from number_guessing_core.leaderboard import LeaderboardEntry
from number_guessing_core.leaderboard_views import filter_score_band

def test_filter_score_band_is_inclusive_and_ranked():
    entries = [LeaderboardEntry("A", 100, 2), LeaderboardEntry("B", 200, 3), LeaderboardEntry("C", 150, 1)]
    assert [e.player for e in filter_score_band(entries, 100, 150)] == ["C", "A"]
