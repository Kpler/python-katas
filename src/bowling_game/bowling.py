class Frame:
    def __init__(self):
        self.first_roll = None
        self.second_roll = None
        self.bonuses = 0

    def score(self):
        return (self.first_roll or 0) + (self.second_roll or 0) + self.bonuses

    def add_roll(self, score):
        if self.first_roll is None:
            self.first_roll = score
        else:
            self.second_roll = score

class Game:

    def __init__(self):
        self.first_roll = True
        #self.current_score = 0
        self.frames = [Frame()]


    def roll(self, score: int):
        first_roll = self.frames[-1].first_roll is None
        self.frames[-1].add_roll(score)
        if not first_roll:
            self.frames.append(Frame())

        if len(self.frames)>1 and self.frames[-2].first_roll == 10:
            self.frames[-2].bonuses= self.frames[-2].bonuses + score

        # self.current_score += score

        # self.frame = self.frame + 1 if not self.first_roll else self.frame
        pass
# TODO : handle strike
    def score(self):
        return sum(frame.score() for frame in self.frames)
