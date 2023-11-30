class TennisGame:

    state = {
        "love": lambda other_score: "15",
        "15": lambda other_score: "30",
        "30": lambda other_score: "40" if other_score != "40" else "deuce",
        "40": lambda other_score: "win",
        "deuce": lambda other_score: "advantage",
    }

    def __init__(self):
        self._score = ['love', 'love']

    @property
    def score(self):
        if self._score[0] == 'advantage':
            return 'advantage player 1'
        if self._score[1] == 'advantage':
            return 'advantage player 2'
        if "deuce" in self._score:
            return "deuce"
        if self._score[0] == 'win':
            return 'Player 1 won'
        if self._score[1] == 'win':
            return 'Player 2 won'
        return '-'.join(self._score)

    def ball_result(self, player: int):
        if player == 1:
            self._score[0] = self.state[self._score[0]](self._score[1])
        elif player == 2:
            self._score[1] = self.state[self._score[1]](self._score[0])
        else:
            raise ValueError


class Player:
    state = {
        "love": lambda player2: "15",
        "15": lambda player2: "30",
        "30": lambda player2: "40" if player2.score != "40" else "deuce",
        "40": lambda player2: "win",
        "deuce": lambda player2: "advantage",
    }

    def __init__(self):
        self.score = 'love'
