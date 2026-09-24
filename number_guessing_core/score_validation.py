def validate_score(score: int) -> int:
    """Validate and return a non-negative integer score."""
    if isinstance(score, bool) or not isinstance(score, int):
        raise TypeError("score must be an integer")
    if score < 0:
        raise ValueError("score must be non-negative")
    return score
