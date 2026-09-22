import pytest
from number_guessing_core.history import GuessHistory, GuessRecord

def test_history_rejects_invalid_status():
    history = GuessHistory()
    with pytest.raises(ValueError):
        history.add(GuessRecord(4, 1, "invalid"))

def test_history_rejects_invalid_record_type():
    with pytest.raises(TypeError):
        GuessHistory().add("record")
