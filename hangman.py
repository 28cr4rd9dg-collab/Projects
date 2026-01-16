import random


def hangman_game():
    """Classic Hangman word guessing game"""
    words = ["python", "hangman", "computer", "programming",
             "developer", "keyboard", "monitor", "algorithm"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n🎮 Welcome to Hangman! 🎮")
    print(f"Guess the word! You have {max_wrong} wrong guesses allowed.\n")

    while wrong_guesses < max_wrong:
        # Display word progress
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(f"Word: {display}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}\n")

        # Check if player won
        if display.replace(" ", "") == secret_word:
            print(f"🏆 You won! The word was: {secret_word}\n")
            return True

        # Get player guess
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess}'.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")
        else:
            print(f"✅ Good guess! '{guess}' is in the word.\n")

    print(f"😢 Game Over! The word was: {secret_word}\n")
    return False


if __name__ == "__main__":
    play_again = True
    while play_again:
        hangman_game()
        play_again = input(
            "Play again?\n\nY for yes or N to quit: ").lower() == "y"
    print("Thanks for playing! 👋\n")
