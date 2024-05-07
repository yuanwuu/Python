import random
import sys


def guess_num(name):

    # game tracking:
    game_count = 0
    player_wins = 0

    def game():
        nonlocal game_count
        nonlocal player_wins

        while True:  # while the game is in action
            game_count += 1
            print(f"\nGame: {game_count}")

            winning_percentage = (player_wins/game_count)*100
            print(f"winning %: {winning_percentage:.2f}%")

            # inputs:
            computerchoice = random.choice('123')
            pythonchoice = int(computerchoice)

            player = input(
                f"\nHello {name},\nam I thinking 1, 2 or 3!\nEnter your guess:\nor 'q' to quit the game\n\n")

            if player.lower() == 'q':
                print(
                    f"\nThanks for playing the game, see you next time {name}!")
                return  # Exit the function if the player decides to quit

            try:  # player may enter anything
                playerchoice = int(player)

            except ValueError:
                input(f"Number only or 'q' to quit the game:\n")
                if input == 'q':
                    # return
                    sys.exit()
                else:
                    continue

            else:
                if playerchoice == pythonchoice:
                    player_wins += 1

                if playerchoice not in [1, 2, 3]:
                    print(f"1, 2 or 3 only.")
                    playagain = input(f"\n{name}, play again? (y/n): ").lower()
                    if playagain == 'y':
                        continue  # Break the loop to replay
                    else:
                        print(
                            f"\nThanks for playing the game,see you next time {name}!")
                        if __name__ == "__main__":
                            # Exit the function if not playing again
                            sys.exit(f"Bye{name}")
                        else:
                            return

                else:
                    print(f"\n{name} = {playerchoice}\nPython = {
                          pythonchoice}")

    return game()


# greeting is done!
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Let's play a number guessing game!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Enter the name of the player"
    )

    args = parser.parse_args()
    guess_num(args.name)
