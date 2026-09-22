import pytest
from number_guessing_core.leaderboard import LeaderboardEntry, rank_entries

def test_rank_entries_normalizes_names_and_ties_deterministically():
    values = [LeaderboardEntry(" bob ", 100, 2), LeaderboardEntry("Alice", 100, 2)]
    assert [x.player for x in rank_entries(values)] == ["Alice", "bob"]

def test_rank_entries_rejects_invalid_score():
    with pytest.raises(ValueError): rank_entries([LeaderboardEntry("A", -1, 1)])

def test_rank_entries_rejects_invalid_attempts():
    with pytest.raises(ValueError): rank_entries([LeaderboardEntry("A", 10, 0)])
