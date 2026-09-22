import pytest
from number_guessing_core.history import GuessHistory, GuessRecord

def test_history_rejects_unknown_status():
    with pytest.raises(ValueError):
        GuessHistory().add(GuessRecord(5, 1, "unknown"))

def test_history_rejects_invalid_attempt_count():
    with pytest.raises(ValueError):
        GuessHistory().add(GuessRecord(5, 0, "correct"))
