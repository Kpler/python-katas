from typing import List


class MolkkyGame:
    def __init__(self) -> None:
        self.status = "ongoing"
        self.pins_down = []
        self.score = 0
        self.failed_attempts = 0

    def kick_pins(self, param):
        self.pins_down = param
        if len(param) == 1:
            self.score += param[0]
        else:
            self.score += len(param)
        if self.score > 50 :
            self.score = 25
        if self.score == 50:
            self.status = "win"
        if len(param) == 0:
            self.failed_attempts += 1