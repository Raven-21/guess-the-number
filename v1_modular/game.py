# -------------------------
# Control Layer
# -------------------------
from v1_modular.data import (
    add_history,
    get_remaining_chance
)

from v1_modular.logic import (
    check_guess,
    is_win,
    is_game_over
)

def handle_round(guess, game_state):
    # Check guess
    result = check_guess(guess, game_state)

    # Add history
    add_history(game_state, guess, result)

    return result

def process_round(guess, game_state):
    # Update state
    result = handle_round(guess, game_state)

    # Check if win for the first time
    is_first_try = (len(game_state["history"]) == 1)

    # Get remaining chance
    remaining_chance = get_remaining_chance(game_state)

    # Decide status
    if is_win(result):
        return {
            "result": result,
            "is_first_try": is_first_try,
            "remaining_chance": remaining_chance,
            "status": "win"
        }

    if is_game_over(remaining_chance):
        return {
            "result": result,
            "is_first_try": is_first_try,
            "remaining_chance": remaining_chance,
            "status": "lose"
        }

    return {
        "result": result,
        "is_first_try": is_first_try,
        "remaining_chance": remaining_chance,
        "status": "continue"
    }
