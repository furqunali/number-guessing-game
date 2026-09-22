import pytest
from number_guessing_core.limits import remaining_attempts
from number_guessing_core.leaderboard import LeaderboardEntry, rank_entries

def test_remaining_attempts():
    assert remaining_attempts(5, 2) == 3
    assert remaining_attempts(None, 9) is None

def test_attempt_limit_must_be_positive():
    with pytest.raises(ValueError):
        remaining_attempts(0, 1)

def test_leaderboard_is_deterministic():
    entries = [LeaderboardEntry("Zed", 900, 2), LeaderboardEntry("Amy", 900, 1)]
    assert rank_entries(entries)[0].player == "Amy"
