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
        if not isinstance(record, GuessRecord):
            raise TypeError("record must be a GuessRecord")
        if isinstance(record.guess, bool) or not isinstance(record.guess, int):
            raise TypeError("guess must be an integer")
        if isinstance(record.attempts, bool) or not isinstance(record.attempts, int) or record.attempts < 1:
            raise ValueError("attempts must be a positive integer")
        if record.status not in {"higher", "lower", "correct"}:
            raise ValueError("status must be higher, lower, or correct")
        self._records.append(record)

    def latest(self) -> GuessRecord | None:
        return self._records[-1] if self._records else None

    def all(self) -> tuple[GuessRecord, ...]:
        return tuple(self._records)

    def summary(self) -> dict[str, int]:
        correct = sum(r.status == "correct" for r in self._records)
        higher = sum(r.status == "higher" for r in self._records)
        lower = sum(r.status == "lower" for r in self._records)
        return {"total": len(self._records), "correct": correct, "higher": higher, "lower": lower}
