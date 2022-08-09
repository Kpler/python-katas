from typing import List


class Game:

    running_score: List[int] = []

    def score(self) -> int:
        score = 0
        for roll in self.running_score:
            score += roll

        return score

    def roll(self, pins: int):
        if pins < 0 or pins > 10:
            raise Exception("We can't score more than 10 pins in a row")
        self.running_score.append(pins)
