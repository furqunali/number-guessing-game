from dataclasses import dataclass
import json

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

    def by_status(self, status: str) -> tuple[GuessRecord, ...]:
        """Return records for a supported outcome without exposing mutable storage."""
        if status not in {"higher", "lower", "correct"}:
            raise ValueError("status must be higher, lower, or correct")
        return tuple(record for record in self._records if record.status == status)

    def best_attempts(self) -> int | None:
        """Return the fewest attempts among successful guesses, if any."""
        successful = [record.attempts for record in self._records if record.status == "correct"]
        return min(successful) if successful else None

    def summary(self) -> dict[str, int]:
        correct = sum(r.status == "correct" for r in self._records)
        higher = sum(r.status == "higher" for r in self._records)
        lower = sum(r.status == "lower" for r in self._records)
        return {"total": len(self._records), "correct": correct, "higher": higher, "lower": lower}

    def to_dict(self) -> dict[str, list[dict[str, int | str]]]:
        """Return a JSON-compatible snapshot of the recorded guesses."""
        return {
            "records": [
                {
                    "guess": record.guess,
                    "attempts": record.attempts,
                    "status": record.status,
                }
                for record in self._records
            ]
        }


def history_to_json(history: GuessHistory) -> str:
    """Serialize guess history to JSON."""
    if not isinstance(history, GuessHistory):
        raise TypeError("history must be a GuessHistory")
    return json.dumps(history.to_dict())


def history_from_json(payload: str) -> GuessHistory:
    """Restore guess history from a JSON snapshot."""
    if not isinstance(payload, str):
        raise TypeError("payload must be a string")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("history payload must contain an object")
    return GuessHistory.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict) -> "GuessHistory":
        """Restore history from a validated JSON-compatible snapshot."""
        if not isinstance(data, dict):
            raise TypeError("history snapshot must be a dictionary")
        records = data.get("records")
        if not isinstance(records, list):
            raise ValueError("history snapshot records must be a list")

        history = cls()
        for item in records:
            if not isinstance(item, dict):
                raise ValueError("history snapshot records must contain dictionaries")
            try:
                record = GuessRecord(
                    guess=item["guess"],
                    attempts=item["attempts"],
                    status=item["status"],
                )
            except KeyError as exc:
                raise ValueError(f"history record is missing {exc.args[0]}") from exc
            history.add(record)
        return history
