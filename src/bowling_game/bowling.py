class Frame:
    def __init__(self):
        self.first_roll = None
        self.second_roll = None

    def score(self):
        return self.first_roll + self.second_roll

    def add_roll(self, score):
        if self.first_roll is None:
            self.first_roll = score
        else:
            self.second_roll = score

class Game:

    def __init__(self):
        self.first_roll = True
        self.current_score = 0
        self.frames = [Frame()]

    # TODO - add the consept of the bonus
    def roll(self, score: int):
        first_roll = self.frames[-1][1] is None
        if first_roll:
            self.frames[-1].add_roll(score)
        # self.current_score += score

        # self.frame = self.frame + 1 if not self.first_roll else self.frame
        pass

    def score(self):
        return self.current_score
