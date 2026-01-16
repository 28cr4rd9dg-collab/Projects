import random


def guess_game():
    """Simple number guessing game"""
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("\n🎮 Welcome to the Guessing Game! 🎮")
    print(f"I'm thinking of a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print(
                    f"❌ Too low! ({max_attempts - attempts} attempts left)\n")
            elif guess > secret_number:
                print(
                    f"❌ Too high! ({max_attempts - attempts} attempts left)\n")
            else:
                print(
                    f"🎉 Correct! You guessed {secret_number} in {attempts} attempts!\n")
                return True
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    print(f"😢 Game Over! The number was {secret_number}.\n")
    return False


if __name__ == "__main__":
    play_again = True
    while play_again:
        guess_game()
        play_again = input(
            "Play again?\n\nY for yes or N to quit: ").lower() == "yes"
    print("Thanks for playing! 👋\n")
