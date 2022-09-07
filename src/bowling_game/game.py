class Game:
    rolls = []
    def roll(self,count):
        self.rolls.append(count)
    def score(self):
        score = sum(self.rolls)
        print(self.rolls)
        return score