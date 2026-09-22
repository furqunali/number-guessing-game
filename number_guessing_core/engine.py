from dataclasses import dataclass
from random import Random

@dataclass(frozen=True)
class GuessResult:
    guess: int
    target: int
    attempts: int
    status: str

class GuessEngine:
    def __init__(self, start: int = 1, end: int = 100, rng: Random | None = None):
        if start >= end:
            raise ValueError("start must be less than end")
        self.start, self.end = int(start), int(end)
        self.rng = rng or Random()
        self.target = None
        self.attempts = 0
        self.finished = False

    def new_round(self) -> int:
        self.target = self.rng.randint(self.start, self.end)
        self.attempts = 0
        self.finished = False
        return self.target

    def guess(self, value: int) -> GuessResult:
        if self.target is None:
            raise RuntimeError("start a round first")
        if self.finished:
            raise RuntimeError("round is already finished")
        value = int(value)
        self.attempts += 1
        if value == self.target:
            self.finished = True
            status = "correct"
        elif value < self.target:
            status = "higher"
        else:
            status = "lower"
        return GuessResult(value, self.target, self.attempts, status)
