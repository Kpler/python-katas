
class Game:
    rolls = []
    current_score = 0

    def score(self) -> int:
      print(self.rolls)
      self.current_score = sum(self.rolls)
      return self.current_score

    def roll(self, pins: int):
      self.rolls.append(pins)
