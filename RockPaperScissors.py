import sys  # search about sys
import random  # allows the game to decide randoms numbers but search about it
from enum import Enum  # search about enum


class RPS(Enum):
    ROCK = 1  # caps constant variables
    PAPER = 2
    SCISSORS = 3


# variable to continue playing without running the code again
playagain = True
# everything need to be indented below while
while playagain:

    playerchoice = input(
        "\nEnter...\n\n 1 = Rock 🪨\n 2 = Paper 📄\n 3 = Scissors: ✂️\n\n")

# int because the answer value is a number
    player = int(playerchoice)
    if player < 1 or player > 3:  # different number than 1 2 3 quits the program with sys
        sys.exit("\nYou must enter 1 or 2 or 3")

    computerchoice = random.choice("123")  # check how these two lines work
    computer = int(computerchoice)

    # used RPS to get rock paper scissors word instead of the number
    # used /.replace RPS, empty/ to replace RPS before the rock paper scissors with an empty space
    print("\nYou chose " + str(RPS(player)).replace("RPS.", ""))
    print("Python chose " + str(RPS(computer)).replace("RPS.", ""))

    if player == 1 and computer == 3:
        print("\n🍾 You win! 🍾")
    elif player == 2 and computer == 1:
        print("\n🎊 You win! 🎊")
    elif player == 3 and computer == 2:
        print("\n🎉 You win! 🎉")
    elif player == computer:
        print("\n😤 It's a tie! 😤")
    else:
        print("\n🐍 Python wins! 🐍\n")
    # code to end the game with playagain or not
    playagain = input("\n Play again? \n\n Y for Yes or \n N to quit\n\n")
    if playagain.lower() == "y":  # .lower to allow y not caps as answer
        continue
    else:
        print("\n    ✋ ✋ ✋ ✋ ✋\n")
        print("Thank you for playing!\n")
        playagain = False
sys.exit("Bye bye! ✋")
