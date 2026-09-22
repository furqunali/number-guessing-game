def score_for_attempts(attempts: int, won: bool) -> int:
    attempts = int(attempts)
    if attempts < 0:
        raise ValueError("attempts cannot be negative")
    return max(0, 1000 - (attempts - 1) * 50) if won and attempts else 0
