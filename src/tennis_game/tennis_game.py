class TennisGame:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()

    @property
    def score(self):
        if "deuce" in [self.p1.score, self.p2.score]:
            return "deuce"
        if self.p1.score == 'win':
            return 'Player 1 won'
        if self.p2.score == 'win':
            return 'Player 2 won'
        return f"{self.p1.score}-{self.p2.score}"

    def ball_result(self, player: int):
        if player == 1:
            self.p1.win_ball(self.p2)
        elif player == 2:
            self.p2.win_ball(self.p1)
        else:
            raise ValueError


class Player:
    state = {
        "love": lambda player2: "15",
        "15": lambda player2: "30",
        "30": lambda player2: "40" if player2.score != "40" else "deuce",
        "40": lambda player2: "win"
    }

    def __init__(self):
        self.score = 'love'

    def win_ball(self, other_player):
        self.score = self.state[self.score](other_player)
