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
        advantage_game = min(self.scores) >= 3
        if advantage_game and self.scores[0] == self.scores[1]:
            return "deuce"
        elif advantage_game and self.scores[0] > self.scores[1]:
            return "advantage player 1"
        elif advantage_game and self.scores[0] < self.scores[1]:
            return "advantage player 2"
        else:
            return f"{self.score_table[self.scores[0]]}-{self.score_table[self.scores[1]]}"

    def register_ball_winner(self, player):
        if player > len(self.scores):
            raise ValueError
        player_index = player - 1
        if self.has_ended():
            raise GameEndedException
        self.scores[player_index] += 1

    def has_ended(self) -> bool:
        for player_score in self.scores:
            player_reached_max_score = player_score >= len(self.score_table) - 1
            player_far_enough_ahead = abs(self.scores[0] - self.scores[1]) > 1
            if player_reached_max_score and player_far_enough_ahead:
                return True
        return False