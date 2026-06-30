# -------------------------
# Persistence
# -------------------------
import json
from game import Game

def save_game(game):
    data = {
        "number": game.number,
        "max_chance": game.max_chance,
        "history": game.history
    }

    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_game():
    try:
        with open("game_history.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return Game(
            number=data["number"],
            max_chance=data["max_chance"],
            history=data["history"]
        ), "loaded"

    except FileNotFoundError:
        return None, "not_found"

    except json.JSONDecodeError:
        return None, "json_error"