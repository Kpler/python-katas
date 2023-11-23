class GameEndedException(Exception):
    pass


class TennisGame():
    score_table = {
        0: "love",
        1: "15",
        2: "30",
        3: "40",
        4: "win"
    }

    def __init__(self):
        self.scores = [0, 0]

    def score(self):
        return f"{self.score_table[self.scores[0]]}-{self.score_table[self.scores[1]]}"

    def register_ball_winner(self, player):
        if player > len(self.scores):
            raise ValueError
        player_index = player - 1
        for player_score in self.scores:
          if player_score >= len(self.score_table) - 1:
              raise GameEndedException
        self.scores[player_index] += 1
