import random
import sys

# Ensure emoji/unicode output works on all consoles (e.g. Windows cp1252)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎉 Welcome to the Number Guessing Game! 🎮")
    print("🤔 I'm thinking of a number between 1 and 100. Can you guess it? 🔢")

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again. 🚀")
            elif guess > number_to_guess:
                print("📈 Too high! Try again. 🪂")
            else:
                print(f"🎉🎉 Congratulations! You guessed the number in {attempts} attempts. �")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a number. 🔢")

if __name__ == "__main__":
    number_guessing_game()