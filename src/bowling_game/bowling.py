class Game:
    
    def __init__(self):
        self.current_score = 0

    def roll(self, score: int):
        self.current_score += score
        pass

    def score(self):
        return self.current_score