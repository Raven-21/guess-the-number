# -------------------------
# Logic Layer
# -------------------------
from data import get_remaining_chance

def check_guess(guess, game_state):
    if guess > game_state["number"]:
        return "high"
    elif guess < game_state["number"]:
        return "low"
    else:
        return "correct"

def is_win(result):
    return result == "correct"

def is_game_over(remaining_chance):
    return remaining_chance == 0