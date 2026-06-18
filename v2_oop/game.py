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

    def play_round(self, guess):
        result = self.check_guess(guess)

        self.add_history(guess, result)

        is_first_try = self.is_first_try()

        remaining_chance = self.get_remaining_chance()

        if result == "correct":
            status = "win"
        elif remaining_chance == 0:
            status = "lose"
        else:
            status = "continue"


        return {
            "result": result,
            "is_first_try": is_first_try,
            "remaining_chance": remaining_chance,
            "status": status
        }