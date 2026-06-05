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