

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
        else:
            self.winner = None
        return self.winner