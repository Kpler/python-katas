from dataclasses import dataclass
from typing import List


@dataclass
class MolkkyGame:
    number_pins_down: List[int] = []
    score: int = 0

    def kick_pins(self, param):
        self.number_pins_down += len(param)
        self.score += param[0]
