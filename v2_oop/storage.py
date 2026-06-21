# storage.py
def save_summary(game):
    with open("game_history.txt", "a", encoding="utf-8") as file:
        file.write("=== GAME SUMMARY ===\n")
        file.write(f"Answer: {game.number}\n")
        file.write(f"Attempts: {len(game.history)}\n")
        file.write("\n")