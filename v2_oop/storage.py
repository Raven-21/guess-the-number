import json

def save_summary(game):
    data = {
        "number": game.number,
        "max_chance": game.max_chance,
        "history": game.history
    }

    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)