from dataclasses import dataclass
from typing import List


@dataclass
class MolkkyGame:
    pins_down: List[int]
    score: int = 0

    def kick_pins(self, param):
        self.pins_down = param
        if len(param) == 1:
            self.score += param[0]
        else:
            self.score += len(param)
