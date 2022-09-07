class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, count):
        self.rolls.append(count)

    def score(self):
        output = 0
        for index,roll in enumerate(self.rolls):
            penultimate_roll = self.rolls[index-2] if index >= 2 else 0
            previous_roll = self.rolls[index-1] if index >= 2 else 0
            if penultimate_roll + previous_roll == 10:
                output += roll*2
            else:
                output += roll
        return output