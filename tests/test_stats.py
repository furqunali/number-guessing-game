import pytest
from number_guessing_core.stats import GuessStats

def test_from_attempts_scores_wins_and_losses():
    assert GuessStats.from_attempts(1, True).score == 1000
    assert GuessStats.from_attempts(3, True).score == 900
    assert GuessStats.from_attempts(3, False).score == 0

def test_from_attempts_rejects_boolean_attempt_count():
    with pytest.raises(TypeError):
        GuessStats.from_attempts(True, True)
