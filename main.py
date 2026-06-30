# -------------------------
# Controller
# -------------------------
from game import Game
from storage import save_game, load_game

from ui import (
    show_result,
    show_summary,
    show_chance,
    show_game_over,
    show_save_not_found,
    show_save_file_broken
)

print("Welcome to Guess the Number! 😀😀😀")

def choose_difficulty():
    while True:
        choice = input(
            "\nChoose Difficulty:\n"
            "1. Easy (10 Chances)\n"
            "2. Hard (5 Chances)\n"
            "Select: "
        )
        if choice == "1":
            return 10
        elif choice == "2":
            return 5
        else:
            print("\nPlease choose 1 or 2.")

# ---------------
# Input
# ---------------
def get_valid_guess():
    while True:
        try:
            print("-------------------------------------------------")
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue
        return guess

# ---------------
# Orchestrator
# ---------------
def start_game():
    while True:
        choice = input(
            "1. New Game\n"
            "2. Load Game\n"
            "3. Exit\n"
            "Select: "
        )

        if choice == "1":
            max_chance = choose_difficulty()
            game = Game(max_chance)
            play_game(game)
            return True

        elif choice == "2":
            game, status = load_game()

            if status == "not_found":
                show_save_not_found()
            elif status == "json_error":
                show_save_file_broken()

            if game is None:
                max_chance = choose_difficulty()
                game = Game(max_chance)

            play_game(game)
            return True

        elif choice == "3":
            print("\nThank you for playing! Goodbye! 😀")
            return False

        else:
            print("Please choose 1, 2, or 3.")

def play_game(game):
    print("Please enter a number between 1 and 100.")
    print(f"You have {game.remaining_chance} chances. Good luck! 😉")

    # Debug
    #print(f"Debug: {game}")

    while True:
        # Get input
        guess = get_valid_guess()

        # Get game data
        data = game.play_round(guess)

        # Debug
        #print(f"Debug: {game}")

        # Show guess result
        show_result(data["result"], data["is_first_try"])

        # Win condition
        if data["status"] == "win":
            show_summary(game)
            save_game(game)
            break

        # Lose condition
        if data["status"] == "lose":
            show_game_over(game.number)
            show_summary(game)
            save_game(game)
            break

        show_chance(data["remaining_chance"])

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ")
        if choice == "y":
            return True
        elif choice == "n":
            print("\nThank you for playing! Goodbye! 😀")
            return False
        else:
            print("Please enter a yes or no!")

# ---------------
# Main Program
# ---------------
while True:
    if not start_game():
        break

    if not play_again():
        break
