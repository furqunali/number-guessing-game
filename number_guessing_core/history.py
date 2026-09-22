from dataclasses import dataclass

@dataclass(frozen=True)
class GuessRecord:
    guess: int
    attempts: int
    status: str

class GuessHistory:
    def __init__(self):
        self._records: list[GuessRecord] = []

    def add(self, record: GuessRecord):
        if record.attempts < 1:
            raise ValueError("attempts must be positive")
        self._records.append(record)

    def latest(self) -> GuessRecord | None:
        return self._records[-1] if self._records else None

    def all(self) -> tuple[GuessRecord, ...]:
        return tuple(self._records)

    def summary(self) -> dict[str, int]:
        """Return deterministic counts for UI and session analytics."""
        correct = sum(record.status == "correct" for record in self._records)
        higher = sum(record.status == "higher" for record in self._records)
        lower = sum(record.status == "lower" for record in self._records)
        return {"total": len(self._records), "correct": correct, "higher": higher, "lower": lower}
