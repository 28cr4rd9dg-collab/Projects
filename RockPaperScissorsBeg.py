import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


games_count = 0
player_wins = 0
python_wins = 0


while True:
    # Player input
    playerchoice = input(
        "\nEnter...\n\n"
        "1 = Rock 🪨\n"
        "2 = Paper 📄\n"
        "3 = Scissors ✂️\n\n"
    )

    if playerchoice not in ["1", "2", "3"]:
        print("\nYou must enter 1, 2, or 3.")
        continue

    player = int(playerchoice)
    computer = random.randint(1, 3)

    # Show choices
    print(f"\nYou chose {RPS(player).name.title()}")
    print(f"Python chose {RPS(computer).name.title()}")

    # Decide winner
    if player == computer:
        print("\n😤 It's a tie! 😤")
    elif (
        (player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)
    ):
        print("\n🎉 You win! 🎉")
        player_wins += 1
    else:
        print("\n🐍 Python wins! 🐍")
        python_wins += 1

    # Game stats
    games_count += 1
    print(f"\nGame count: {games_count}")
    print(f"Player wins: {player_wins}")
    print(f"Python wins: {python_wins}")

    # Play again
    playagain = input("\nPlay again? (Y/N): ").lower()
    if playagain != "y":
        print("\n✋ Thanks for playing! ✋\n")
        sys.exit()
