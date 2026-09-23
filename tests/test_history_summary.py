from number_guessing_core.history import GuessHistory, GuessRecord

def test_history_summary_counts_statuses():
    history = GuessHistory()
    history.add(GuessRecord(10, 1, "higher"))
    history.add(GuessRecord(20, 2, "lower"))
    history.add(GuessRecord(15, 3, "correct"))
    assert history.summary() == {"total": 3, "correct": 1, "higher": 1, "lower": 1}

def test_empty_history_summary_is_zeroed():
    assert GuessHistory().summary() == {"total": 0, "correct": 0, "higher": 0, "lower": 0}


from number_guessing_core.history import GuessHistory, GuessRecord
def test_history_summary_counts_statuses():
    history = GuessHistory()
    for record in (GuessRecord(5,1,"higher"), GuessRecord(7,2,"lower"), GuessRecord(8,3,"correct")): history.add(record)
    assert history.summary() == {"total": 3, "correct": 1, "higher": 1, "lower": 1}
