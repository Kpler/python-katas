class Game:
    
    def __init__(self):
        self.first_roll = True
        self.current_score = 0
        self.frame = 0

    # TODO - add the consept of the bonus
    def roll(self, score: int):
        self.current_score += score
        self.frame = self.frame + 1 if not self.first_roll else self.frame
        pass

    def score(self):
        return self.current_score