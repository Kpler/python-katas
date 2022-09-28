class Game(object):

    def __init__(self):
        self.player1_score = "love"
        self.player2_score = "love"

    def score(self):
        return f"{self.player1_score}-{self.player2_score}"