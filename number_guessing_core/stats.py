from dataclasses import dataclass

@dataclass(frozen=True)
class GuessStats:
    attempts: int
    won: bool
    score: int

    @classmethod
    def from_attempts(cls, attempts: int, won: bool) -> "GuessStats":
        if isinstance(attempts, bool) or not isinstance(attempts, int):
            raise TypeError("attempts must be an integer")
        if attempts < 0:
            raise ValueError("attempts cannot be negative")
        score = max(0, 1000 - max(0, attempts - 1) * 50) if won else 0
        return cls(attempts, bool(won), score)
