class Game:
    def __init__(self):
        self._score = ['love', 'love']
        self.winner = None
        self.advantage = None

    @property
    def score(self):
        if self.winner is not None:
            return f"Player {self.winner} wins"
        if self.advantage is not None:
            return f"Advantage player {self.advantage}"
        if self._score == ['40', '40']:
            return "deuce"
        return '-'.join(self._score)

    def ball_result(self, player: int):
        score_index = player - 1
        if self._score[score_index] == 'love':
            self._score[score_index] = '15'
        elif self._score[score_index] == '15':
            self._score[score_index] = '30'
        elif self._score[score_index] == '30':
            self._score[score_index] = '40'
        elif self.advantage != player and self.advantage is not None:
            self.advantage = None
        # TODO: fix here
        elif self._score == ['40', '40']:
            self.advantage = player
        elif self._score[score_index] == '40':
            self.winner = player
