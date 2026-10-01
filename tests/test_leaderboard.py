from number_guessing_core import LeaderboardEntry, leaderboard_from_dict, leaderboard_to_dict, top_entries

def test_top_entries_limits_ranked_results():
    entries = [LeaderboardEntry("A", 100, 2), LeaderboardEntry("B", 300, 3), LeaderboardEntry("C", 200, 1)]
    assert [entry.player for entry in top_entries(entries, 2)] == ["B", "C"]


def test_leaderboard_snapshot_round_trips_through_json():
    import json

    entries = [
        LeaderboardEntry("Bravo", 700, 3),
        LeaderboardEntry("Alpha", 900, 2),
    ]
    snapshot = leaderboard_to_dict(entries)
    restored = leaderboard_from_dict(json.loads(json.dumps(snapshot)))

    assert restored == [
        LeaderboardEntry("Alpha", 900, 2),
        LeaderboardEntry("Bravo", 700, 3),
    ]


def test_leaderboard_snapshot_rejects_malformed_data():
    import pytest

    with pytest.raises(TypeError):
        leaderboard_from_dict([])

    with pytest.raises(ValueError):
        leaderboard_from_dict({"entries": "not-a-list"})

    with pytest.raises(ValueError):
        leaderboard_from_dict({"entries": [{"player": "A", "score": 10}]})
