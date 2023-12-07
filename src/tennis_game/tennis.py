class Game:
    def __init__(self):
        self._score = ['love', 'love']

    @property
    def score(self):
        return '-'.join(self._score)

    def ball_result(self, player: int):
        # _increment_score(player)
#