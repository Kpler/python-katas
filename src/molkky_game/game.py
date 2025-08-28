from dataclasses import dataclass

@dataclass
class MolkkyGame:
    numberPinsDown: int[] = []
    score: int = 0

    def kickPins(self, param):
        self.numberPinsDown += len(param)
        self.score += param[0]
