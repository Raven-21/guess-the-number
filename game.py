# -------------------------
# Business
# -------------------------
import random

class Game:

    def __init__(self, max_chance, number=None, history=None):
        if number is None:
            self.number = random.randint(1, 100)
        else:
            self.number = number

        self.max_chance = max_chance
        
        if history is None:
            self.history = []
        else:
            self.history = history

    @property
    def remaining_chance(self):
        return self.max_chance - len(self.history)

    @property
    def is_first_try(self):
        return len(self.history) == 1

    def __str__(self):
        return (
            f"Game("
            f"answer={self.number}, "
            f"max_chance={self.max_chance}, "
            f"attempts={len(self.history)}, "
            f"remaining={self.remaining_chance}"
            f")"
        )

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

    def check_guess(self, guess):
        if guess > self.number:
            return "high"
        elif guess < self.number:
            return "low"
        else:
            return "correct"

    def play_round(self, guess):
        result = self.check_guess(guess)

        self.add_history(guess, result)

        if result == "correct":
            status = "win"
        elif self.remaining_chance == 0:
            status = "lose"
        else:
            status = "continue"

        return {
            "result": result,
            "is_first_try": self.is_first_try,
            "remaining_chance": self.remaining_chance,
            "status": status
        }