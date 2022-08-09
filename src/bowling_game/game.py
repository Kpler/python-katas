
class Game:

    running_score: int = 0

    def score(self) -> int:
        return self.running_score

    def roll(self, pins: int):
        if not (0<pins<10):
            raise Exception("We can't score more than 10 pins in a row")
        self.running_score += pins
