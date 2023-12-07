class Game:
    def __init__(self):
        self._score = ['love', 'love']

    @property
    def score(self):
        return '-'.join(self._score)

    def ball_result(self, player: int):
        score_index = player - 1
        if self._score[score_index] == 'love':
            self._score[score_index] = '15'
        elif self._score[score_index] == '15':
            self._score[score_index] = '30'
        elif self._score[score_index] == '30':
            self._score[score_index] = '40'

