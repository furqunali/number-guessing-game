from random import Random

import pytest

from number_guessing_core import GuessEngine


def test_new_round_uses_injected_random_generator():
    engine = GuessEngine(start=1, end=10, rng=Random(7))

    target = engine.new_round()

    assert target == 6
    assert engine.attempts == 0
    assert engine.finished is False


def test_guess_reports_direction_and_finishes_on_correct_guess():
    engine = GuessEngine(start=1, end=10, rng=Random(7))
    engine.new_round()

    assert engine.guess(3).status == "higher"
    result = engine.guess(6)

    assert result.status == "correct"
    assert result.attempts == 2
    assert engine.finished is True


def test_guess_requires_active_round_and_rejects_finished_round():
    engine = GuessEngine(start=1, end=10, rng=Random(7))

    with pytest.raises(RuntimeError):
        engine.guess(5)

    engine.new_round()
    engine.guess(6)

    with pytest.raises(RuntimeError):
        engine.guess(6)


def test_engine_requires_ordered_bounds():
    with pytest.raises(ValueError):
        GuessEngine(start=10, end=10)
