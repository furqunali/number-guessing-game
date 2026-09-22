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
