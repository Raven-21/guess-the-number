# -------------------------
# Presentation Layer
# -------------------------
from v1_modular.data import get_stats

def show_result(result, is_first_try):
    if result == "high":
        print("Too High. ❌")
    elif result == "low":
        print("Too low. ❌")
    else:
        if is_first_try:
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