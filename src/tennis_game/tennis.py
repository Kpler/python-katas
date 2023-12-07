

class Game():
    player1_points = 0
    player2_points = 0
    player1_score = "love"
    player2_score = "love"
    winner = None

    def __int__(self):
        pass

    def get_winner(self):
        self.winner = None
        if self.player1_points == 4:
            self.winner = "player1"
        elif self.player2_points == 4:
            self.winner = "player2"
        return self.winner
    
    def get_score(self):
        if self.player1_score == self.player2_score and self.player1_score == "40":
            return "deuce"
        return f"{self.player1_score}:{self.player2_score}"