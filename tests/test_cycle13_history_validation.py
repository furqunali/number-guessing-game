import pytest
from number_guessing_core.history import GuessHistory, GuessRecord

def test_history_rejects_unknown_status():
    with pytest.raises(ValueError):
        GuessHistory().add(GuessRecord(2, 1, "unknown"))
