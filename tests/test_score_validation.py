import pytest
from number_guessing_core.score_validation import validate_score

def test_validate_score_accepts_zero_and_positive_values():
    assert validate_score(0) == 0
    assert validate_score(250) == 250

@pytest.mark.parametrize("value", [-1, True, 1.5])
def test_validate_score_rejects_invalid_values(value):
    with pytest.raises((TypeError, ValueError)):
        validate_score(value)
