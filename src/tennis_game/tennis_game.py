

class TennisGame():

    score_table = {
        0: "love",
        # 1: "15",
        # 2: "30",
        # 3: "40"
    }

    def __init__(self):
        self.scores = [0, 0]

    def score(self):
        return f"{self.score_table[self.scores[0]]}-{self.score_table[self.scores[1]]}"

    def register_ball_winner(self, player):
        if player > len(self.scores):
            raise ValueError
        self.scores[player] += 1
