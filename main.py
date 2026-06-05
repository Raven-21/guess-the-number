from data import(
    create_game_state,
    get_remaining_chance
)

from logic import check_guess

from ui import(
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
def get_guess():
    try:
        print("-------------------------------------------------")
        guess = int(input("Guess the number: "))
        return guess
    except ValueError:
        print("Please enter a valid number!")
        return None

# -------------------------
# Control Layer
# -------------------------
def handle_round(guess, game_state):
    # Check guess
    result = check_guess(guess, game_state)
    # Check trying to win for the first time
    is_first_try = (len(game_state["history"]) == 0)

    # Add history
    game_state["history"].append({
        "guess": guess,
        "result": result
    })

    # Show result
    show_result(result, is_first_try)

    return result

def play_game():
    max_chance = choose_difficulty()
    game_state = create_game_state(max_chance)

    print(f"You have {game_state['max_chance']} chances. Good luck! 😉")
    print(game_state["number"])

    while True:
        # Get input
        guess = get_guess()
        if guess is None:
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue

        # Get the result of each round
        result = handle_round(guess, game_state)

        # Get remaining chance
        remaining_chance = get_remaining_chance(game_state)

        # Win condiction
        if result == "correct":
            show_summary(game_state)
            break

        # Lose condition
        if remaining_chance == 0:
            show_game_over(game_state["number"])
            show_summary(game_state)
            break

        show_chance(game_state)

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