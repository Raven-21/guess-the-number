import random

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
# Data Layer
# -------------------------
def create_game_state():
    return {
        "number": random.randint(1, 100),
        "max_chance": choose_difficulty(),
        "history": []
    }

def get_stats(game_state):
    stats = {"high": 0, "low": 0, "correct": 0}

    for record in game_state["history"]:
        stats[record["result"]] += 1

    return stats

def get_remaining_chance(game_state):
    return game_state["max_chance"] - len(game_state["history"])

# -------------------------
# Logic Layer
# -------------------------
def check_guess(guess, game_state):
    if guess > game_state["number"]:
        return "high"
    elif guess < game_state["number"]:
        return "low"
    else:
        return "correct"

# -------------------------
# Presentation Layer
# -------------------------
def show_result(result, first_try):
    if result == "high":
        print("Too High. ❌")
    elif result == "low":
        print("Too low. ❌")
    else:
        if first_try == 1:
            print("Unbelievable!!! 😮😮😮 You just guessed it right in 1 time! ✅")
        else:
            print("Congratulations! 😁😁😁 You guessed it right. ✅")

def show_history(game_state):
    print("\nGuess History:")
    for record in game_state["history"]:
        print(f"{record['guess']} → {record['result']}")

def show_stats(game_state):
    stats = get_stats(game_state)

    print("\nGuess Stats:")
    for key, value in stats.items():
        print(f"{key}: {value}")

def show_summary(game_state):
    print("\n=== GAME SUMMARY ===")
    show_history(game_state)
    show_stats(game_state)

def show_chance(chance):
    if chance > 1:
        print(f"You have {chance} more chances.")
    elif chance == 1:
        print("You only get 1 chance. Keep it up! 🦾🦾🦾")

def show_game_over(answer):
    print("Sorry! Game Over! 😥😥😥")
    print(f"The answer is {answer}.")

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
    game_state = create_game_state()

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

        show_chance(remaining_chance)

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