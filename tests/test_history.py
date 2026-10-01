import pytest
from number_guessing_core.history import GuessHistory, GuessRecord
from number_guessing_core.scoring import score_for_attempts

def test_history_keeps_latest_guess():
    history = GuessHistory()
    history.add(GuessRecord(20, 1, "higher"))
    history.add(GuessRecord(50, 2, "correct"))
    assert history.latest().guess == 50

def test_history_reports_best_successful_attempt_count():
    history = GuessHistory()
    assert history.best_attempts() is None
    history.add(GuessRecord(20, 4, "higher"))
    history.add(GuessRecord(50, 7, "correct"))
    history.add(GuessRecord(42, 3, "correct"))
    assert history.best_attempts() == 3

def test_scoring_is_bounded():
    assert score_for_attempts(1, True) == 1000
    assert score_for_attempts(30, True) == 0
    with pytest.raises(ValueError):
        score_for_attempts(-1, True)


def test_history_snapshot_round_trips_through_json():
    import json

    history = GuessHistory()
    history.add(GuessRecord(20, 1, "higher"))
    history.add(GuessRecord(50, 2, "correct"))

    snapshot = history.to_dict()
    restored = GuessHistory.from_dict(json.loads(json.dumps(snapshot)))

    assert restored.all() == history.all()
    assert restored.summary() == history.summary()


def test_history_snapshot_rejects_malformed_data():
    with pytest.raises(TypeError):
        GuessHistory.from_dict([])

    with pytest.raises(ValueError):
        GuessHistory.from_dict({"records": "not-a-list"})

    with pytest.raises(ValueError):
        GuessHistory.from_dict({"records": [{"guess": 10, "attempts": 1}]})
