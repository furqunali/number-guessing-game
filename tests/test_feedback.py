import pytest

from number_guessing_core.feedback import feedback_distance, guess_feedback


def test_guess_feedback_direction():
    assert guess_feedback(4, 10) == "too_low"
    assert guess_feedback(16, 10) == "too_high"
    assert guess_feedback(10, 10) == "correct"


def test_feedback_distance_is_absolute():
    assert feedback_distance(4, 10) == 6
    assert feedback_distance(13, 10) == 3


def test_feedback_rejects_boolean_inputs():
    with pytest.raises(TypeError):
        guess_feedback(True, 10)
