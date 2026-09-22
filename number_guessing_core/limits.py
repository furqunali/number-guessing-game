def validate_attempt_limit(limit: int | None) -> int | None:
    if limit is None:
        return None
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("attempt limit must be an integer")
    if limit < 1:
        raise ValueError("attempt limit must be positive")
    return limit

def remaining_attempts(limit: int | None, attempts: int) -> int | None:
    limit = validate_attempt_limit(limit)
    if isinstance(attempts, bool) or not isinstance(attempts, int):
        raise TypeError("attempts must be an integer")
    attempts = max(0, attempts)
    return None if limit is None else max(0, limit - attempts)

def difficulty_for_limit(limit: int | None) -> str:
    """Classify the configured attempt budget for UI and analytics."""
    limit = validate_attempt_limit(limit)
    if limit is None:
        return "unlimited"
    if limit <= 3:
        return "hard"
    if limit <= 6:
        return "normal"
    return "easy"
