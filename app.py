import sys

from number_guessing_core import GuessEngine, GuessHistory, GuessRecord, GuessStats


try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def number_guessing_game() -> None:
    engine = GuessEngine()
    history = GuessHistory()
    engine.new_round()

    print("🎉 Welcome to the Number Guessing Game! 🎮")
    print("🤔 I'm thinking of a number between 1 and 100. Can you guess it? 🔢")

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            result = engine.guess(guess)
            history.add(
                GuessRecord(
                    guess=result.guess,
                    attempts=result.attempts,
                    status=result.status,
                )
            )

            if result.status == "higher":
                print("📉 Too low! Try again. 🚀")
            elif result.status == "lower":
                print("📈 Too high! Try again. 🪂")
            else:
                stats = GuessStats.from_attempts(result.attempts, won=True)
                print(
                    f"🎉🎉 Congratulations! You guessed the number "
                    f"in {result.attempts} attempts. 🎯"
                )
                print(f"📊 Final score: {stats.score}")
                print(f"🧾 Guess history: {history.summary()}")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a number. 🔢")


if __name__ == "__main__":
    number_guessing_game()
