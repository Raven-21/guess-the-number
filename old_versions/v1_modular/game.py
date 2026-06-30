# -------------------------
# Control Layer
# -------------------------
from v1_modular.data import (
    add_history,
    is_first_try,
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
    first_try = is_first_try(game_state)

    # Get remaining chance
    remaining_chance = get_remaining_chance(game_state)

    # Decide status
    if is_win(result):
        return {
            "result": result,
            "first_try": first_try,
            "remaining_chance": remaining_chance,
            "status": "win"
        }

    if is_game_over(remaining_chance):
        return {
            "result": result,
            "first_try": first_try,
            "remaining_chance": remaining_chance,
            "status": "lose"
        }

    return {
        "result": result,
        "first_try": first_try,
        "remaining_chance": remaining_chance,
        "status": "continue"
    }
