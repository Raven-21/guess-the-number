from v1_modular.data import create_game_state

from v1_modular.game import process_round

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
# Control Layer
# -------------------------
def play_game():
    max_chance = choose_difficulty()
    game_state = create_game_state(max_chance)

    print(f"You have {game_state['max_chance']} chances. Good luck! 😉")
    print(game_state["number"])

    while True:
        # Get input
        guess = get_valid_guess()

        # Get game result
        status = process_round(guess, game_state)

        # 👉 WIN CONDITION
        if status == "win":
            break

        # 👉 LOSE CONDITION
        if status == "lose":
            break

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