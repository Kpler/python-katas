from dataclasses import dataclass

@dataclass
class MolkkyGame:
    score: int = 0
    numberPinsDown: int = 0

    def kickPins(self, param):
        self.numberPinsDown += len(param)
        self.score += param[0]
