
class Game:
    current_score = 0

    def score(self) -> int:
        return self.current_score

    def roll(self, pins: int):
        self.current_score += pins
