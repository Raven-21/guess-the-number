# -------------------------
# Presentation
# -------------------------
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

def show_history(game):
    print("\nGuess History:")
    for record in game.history:
        print(f"{record['guess']} → {record['result']}")

def show_stats(game):
    stats = game.get_stats()

    print("\nGuess Stats:")
    for key, value in stats.items():
        print(f"{key}: {value}")

def show_summary(game):
    print("\n=== GAME SUMMARY ===")
    show_history(game)
    show_stats(game)

def show_chance(chance):
    if chance > 1:
        print(f"You have {chance} more chances.")
    elif chance == 1:
        print("You only get 1 chance. Keep it up! 🦾🦾🦾")

def show_game_over(answer):
    print("Sorry! Game Over! 😥😥😥")
    print(f"The answer is {answer}.")

def show_save_not_found():
    print("No save file found. Starting a new game.")

def show_save_file_broken():
    print("Save file is corrupted. Starting a new game.")