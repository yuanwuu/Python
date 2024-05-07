from guess_number import guess_num
import rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Welcome to the Arcade Game Center!"
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help="Enter the name of player"
    )

    args = parser.parse_args()

player_choice = input(
    f"\nHi {args.name},\nPlease choose a game:\n\n1 = Rock Paper Scissors\n2 = Guess My Number\n\n")

while True:
    if player_choice == '1':
        print('rps need work')
    elif player_choice == '2':
        guess_num(args.name)
    else:
        input(f"{args.name}, please enter a number or 'x' to quit\n\n")
    break
