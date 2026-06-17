import random

class Game:

    def __init__(self, max_chance):
        self.number = random.randint(1, 100)
        self.max_chance = max_chance
        self.history = []

    def add_history(self, guess, result):
        self.history.append({
            "guess": guess,
            "result": result
        })

    def get_stats(self):
        stats = {"high": 0, "low": 0, "correct": 0}

        for record in self.history:
            stats[record["result"]] += 1

        return stats

    def is_first_try(self):
        return len(self.history) == 1

    def get_remaining_chance(self):
        return self.max_chance - len(self.history)

    def check_guess(self, guess):
        if guess > self.number:
            return "high"
        elif guess < self.number:
            return "low"
        else:
            return "correct"

game = Game(10)

game.add_history(1, "low")
game.add_history(10, "high")

print(game.get_stats())