import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

        # print(RPS(2))  # RPS.PAPER
        # print(RPS.ROCK)  # RPS.ROCK
        # print(RPS['ROCK'])  # RPS.ROCK
        # print(RPS.ROCK.value)  # 1
        # sys.exit() # when run, everything stop from here

    playerchoice = input(
        'Enter ... \n1 for Rocks,\n2 for Paper, or \n3 for Scissors:\n\n')

    if playerchoice not in ['1', '2', '3']:
        print('You much enter 1, 2 or 3.')
        return play_rps

    player = int(playerchoice)

    computerchoice = random.choice('123')

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".\n")
    print("\nPython chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")

    print('\nPlay again?')
    while True:
        playagain = input('\nY for Yes or \nQ to Quit. \n')
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break

    if playagain.lower() == 'y':
        return play_rps()
    else:
        print('Thanks for playing the game!\n ')
        sys.exit('Bye!')


play_rps()
