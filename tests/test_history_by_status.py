import pytest
from number_guessing_core.history import GuessHistory, GuessRecord

def test_by_status_returns_matching_records_in_order():
    history = GuessHistory()
    first = GuessRecord(2, 1, "higher")
    second = GuessRecord(4, 2, "correct")
    history.add(first)
    history.add(second)
    assert history.by_status("higher") == (first,)

def test_by_status_rejects_unknown_status():
    with pytest.raises(ValueError):
        GuessHistory().by_status("unknown")
