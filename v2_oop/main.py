from v2_oop.game import Game
from v2_oop.storage import save_summary

from v2_oop.ui import (
    show_result,
    show_summary,
    show_chance,
    show_game_over
)

# -------------------------
# Initialization
# -------------------------
print("Welcome to Guess the Number! 😀😀😀")
print("Please enter a number between 1 and 100.")

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

# -------------------------
# Input Layer
# -------------------------
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

# -------------------------
# Orchestrator Layer
# -------------------------
def play_game():
    max_chance = choose_difficulty()
    game = Game(max_chance)

    print(f"You have {game.max_chance} chances. Good luck! 😉")
    #print(game.number)

    while True:
        # Get input
        guess = get_valid_guess()

        # Get game data
        data = game.play_round(guess)

        show_result(data["result"], data["is_first_try"])

        # Win condition
        if data["status"] == "win":
            show_summary(game)
            save_summary(game)
            break

        # Lose condition
        if data["status"] == "lose":
            show_game_over(game.number)
            show_summary(game)
            save_summary(game)
            break

        show_chance(data["remaining_chance"])

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ")
        if choice == "y":
            return True
        elif choice == "n":
            print("\nThank you for playing! 😀")
            return False
        else:
            print("Please enter a yes or no!")

# -------------------------
# Main Program
# -------------------------
while True:
    play_game()

    if not play_again():
        break
