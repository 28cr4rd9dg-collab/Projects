import sys  # search sys
import random  # random is for python to generate random numbers
from enum import Enum  # search enum


def rps():
    games_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins  # search nonlocal
        nonlocal python_wins
        nonlocal games_count

        class RPS(Enum):  # 4 lines used to visualize words instead of numbers as a game result
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter...\n\n 1 = Rock 🪨\n 2 = Paper 📄\n 3 = Scissors ✂️\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print("\nYou must enter 1 or 2 or 3")
            return play_rps()  # search return vs continue

        player = int(playerchoice)
        computer = int(random.choice("123"))
        # .replace used to replace RPS word with an empty space
        print(
            f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}."
        )
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "\n🍾 You win! 🍾"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "\n🎊 You win! 🎊"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "\n🎉 You win! 🎉"
            elif player == computer:
                return "\n😤 It's a tie! 😤"
            else:
                python_wins += 1
                return "\n🐍 Python wins! 🐍\n"

        game_results = decide_winner(player, computer)
        print(game_results)

        games_count += 1

        print(f"\nGames count: {games_count}")
        print(f"Player victories: {player_wins}")
        print(f"Python victories: {python_wins}")

        # while allows the game to continue until we select n to quit
        while True:
            playagain = input(
                "\nPlay again?\nY for Yes\nN to quit\n\n"
            ).lower()
            if playagain in ["y", "n"]:
                break

        if playagain == "y":
            return play_rps()
        else:
            print("\n✋ Thank you for playing! ✋\n")
            sys.exit("          Bye bye!\n")

    return play_rps


rock_paper_scissors = rps()

rock_paper_scissors = rps()
rock_paper_scissors()
