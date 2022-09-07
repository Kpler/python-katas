class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, count):
        self.rolls.append(count)

    def score(self):
        output = 0
        for index,roll in enumerate(self.rolls):
            is_even = index%2 == 0
            penultimate_roll = self.rolls[index-2] if index >= 2 else 0
            previous_roll = self.rolls[index-1] if index >= 2 else 0
            output += roll
            if penultimate_roll + previous_roll == 10 and is_even:
                output += roll
        return output