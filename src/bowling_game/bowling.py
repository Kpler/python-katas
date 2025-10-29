

class Game:


    def __init__(self):
        self.rolls = [0]*21
        self.current_roll = 0
        self.score = 0

    def roll(self,pins:int):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self, score:int):
        self.score += score