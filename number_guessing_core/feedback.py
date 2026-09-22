def guess_feedback(guess: int, target: int) -> str:
    """Return deterministic feedback for a valid integer guess."""
    if isinstance(guess, bool) or not isinstance(guess, int):
        raise TypeError("guess must be an integer")
    if isinstance(target, bool) or not isinstance(target, int):
        raise TypeError("target must be an integer")
    if guess == target:
        return "correct"
    return "too_low" if guess < target else "too_high"


def feedback_distance(guess: int, target: int) -> int:
    """Return the absolute numeric distance from the target."""
    guess_feedback(guess, target)
    return abs(guess - target)
