
class Game:
    rolls = []
    current_score = 0

    # [3, 7, 1, 2]
    #  0  1   2  3  4
    # [3, 7 + 1, 1, 2]

    def score(self) -> int:
        for i , value in enumerate(self.rolls):
            self.current_score
            if i % 2 != 0 and sum(self.rolls[i-2], self.rolls[i-1]) == 10:


      if (pins + self.rolls[self.rolls.length - 1]) == 10:
        self.current_score = sum(self.rolls)
      return self.current_score

    def roll(self, pins: int):
      self.rolls.append(pins)
