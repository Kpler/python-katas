
class Game:

    running_score: int = 0

    def score(self) -> int:
        return self.running_score

    def roll(self, pins: int):
        self.running_score += pins
