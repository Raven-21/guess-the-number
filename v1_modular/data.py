# -------------------------
# Data Layer
# -------------------------
import random

def create_game_state(max_chance):
    return {
        "number": random.randint(1, 100),
        "max_chance": max_chance,
        "history": []
    }

def add_history(game_state, guess, result):
    game_state["history"].append({
        "guess": guess,
        "result": result
    })

def get_stats(game_state):
    stats = {"high": 0, "low": 0, "correct": 0}

    for record in game_state["history"]:
        stats[record["result"]] += 1

    return stats

def is_first_try(game_state):
    return len(game_state["history"]) == 1

def get_remaining_chance(game_state):
    return game_state["max_chance"] - len(game_state["history"])