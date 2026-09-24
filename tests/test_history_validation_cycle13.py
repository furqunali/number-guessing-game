from number_guessing_core.history import GuessHistory, GuessRecord


def test_history_records_and_summarizes_valid_records():
    history = GuessHistory()
    history.add(GuessRecord(8, 1, "correct"))
    assert history.summary() == {"total": 1, "correct": 1, "higher": 0, "lower": 0}
