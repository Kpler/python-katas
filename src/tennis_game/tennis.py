class Game:

    player_1_score = 0
    player_2_score = 0
    score_labels = ["love", "15", "30", "40"]

    def __int__(self):
        pass

    def player_1_scored(self):
        self.player_1_score += 1

    def player_2_scored(self):
        self.player_2_score += 1

    def is_finished(self):
        if self.player_1_score > 3 or self.player_2_score > 3:
            return True
        return False

    def get_score(self):
        if self.is_finished():
            return "Player 1 wins"
        return f"{self.score_labels[self.player_1_score]}-{self.score_labels[self.player_2_score]}"
