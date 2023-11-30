class TennisGame:
    def __init__(self):
        pass

    @property
    def score(self):
        return 'love-love'


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
