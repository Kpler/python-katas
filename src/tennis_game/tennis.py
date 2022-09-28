from enum import Enum


class Player(Enum):
    ONE = 'one'
    TWO = 'two'


class Tennis:
    current_player: str
    game_score: dict
    match_score: dict

    def __init__(self) -> None:
        self.game_score = {Player.ONE: 0, Player.TWO: 0}
        self.match_score = {Player.ONE: 0, Player.TWO: 0}

    def play(self, winner: Player):
        current_winner_score = self.game_score.get(winner)
        if current_winner_score == 0:
            self.game_score[winner] = 15
        elif current_winner_score == 15:
            self.game_score[winner] = 30
        elif current_winner_score == 30:
            self.game_score[winner] = 40
        elif current_winner_score == 40:
            self.game_score[winner] = 0
            self.match_score[winner] += 1

    def get_game_score(self):
        return self.game_score

    def get_match_score(self):
        return self.match_score
