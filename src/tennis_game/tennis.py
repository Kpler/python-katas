from enum import Enum


class Player(Enum):
    ONE = 'one'
    TWO = 'two'

class Score(Enum):
    LOVE = 0
    FIFTEEN = 15
    THIRTY = 30
    FORTY = 40
    ADVANTAGE = "A"

class GameScore(TypedDict):
    player: Player
    score: Score

class Tennis:
    current_player: str
    game_score: GameScore
    match_score: dict

    def __init__(self) -> None:
        self.game_score = {Player.ONE: Score.LOVE, Player.TWO: Score.LOVE}
        self.match_score = {Player.ONE: Score.LOVE, Player.TWO: Score.LOVE}

    def play(self, winner: Player):
        current_winner_score = self.game_score.get(winner)
        if current_winner_score == Score.LOVE:
            self.game_score[winner] = Score.FIFTEEN
        elif current_winner_score == Score.FIFTEEN:
            self.game_score[winner] = Score.THIRTY
        elif current_winner_score == Score.THIRTY:
            self.game_score[winner] = Score.FORTY

        elif current_winner_score == Score.FORTY:
            self.game_score[winner] = Score.LOVE
            self.match_score[winner] += 1

    def get_game_score(self):
        return self.game_score

    def get_match_score(self):
        return self.match_score
