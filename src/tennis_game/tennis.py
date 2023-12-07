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

    def update_advantage_game(self, player: int):
        if self.advantage is None:
            self.advantage = player
        elif self.advantage != player:
            self.advantage = None
        else:
            self.winner = player

    def early_game_ball_result(self, player: int):
        score_index = player - 1
        if self._score[score_index] == 'love':
            self._score[score_index] = '15'
        elif self._score[score_index] == '15':
            self._score[score_index] = '30'
        elif self._score[score_index] == '30':
            self._score[score_index] = '40'
        elif self._score[score_index] == '40':
            self.winner = player

    def ball_result(self, player: int):
        if not self.is_end_game():
            self.early_game_ball_result(player=player)
        else:
            self.update_advantage_game(player=player)

    def is_end_game(self):
        return self._score == ["40", "40"]
