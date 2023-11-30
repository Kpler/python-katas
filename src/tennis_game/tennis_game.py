class TennisGame:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()

    @property
    def score(self):
        if self.p1.score == 'win':
            return 'Player 1 won'
        if self.p2.score == 'win':
            return 'Player 2 won'
        return f"{self.p1.score}-{self.p2.score}"

    def ball_result(self, player: int):
        if player == 1:
            self.p1.win_ball()
        elif player == 2:
            self.p2.win_ball()
        else:
            raise ValueError


class Player:
    state = {
        "love": "15",
        "15": "30",
        "30": "40",
        "40": "win"
    }

    def __init__(self):
        self.score = 'love'

    def win_ball(self):
        self.score = self.state[self.score]
