import pytest
from number_guessing_core.history import GuessHistory, GuessRecord
from number_guessing_core.scoring import score_for_attempts

def test_history_keeps_latest_guess():
    history = GuessHistory()
    history.add(GuessRecord(20, 1, "higher"))
    history.add(GuessRecord(50, 2, "correct"))
    assert history.latest().guess == 50

def test_scoring_is_bounded():
    assert score_for_attempts(1, True) == 1000
    assert score_for_attempts(30, True) == 0
    with pytest.raises(ValueError):
        score_for_attempts(-1, True)
