def validate_attempt_limit(limit: int | None) -> int | None:
    if limit is None:
        return None
    value = int(limit)
    if value < 1:
        raise ValueError("attempt limit must be positive")
    return value

def remaining_attempts(limit: int | None, attempts: int) -> int | None:
    limit = validate_attempt_limit(limit)
    attempts = max(0, int(attempts))
    return None if limit is None else max(0, limit - attempts)
