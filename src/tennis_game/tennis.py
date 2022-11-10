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
        self.score_advantage = {Player.ONE: 0, Player.TWO: 0}
        self.match_score = {Player.ONE: 0, Player.TWO: 0}

    def play(self, winner: Player):
        current_winner_score = self.game_score.get(winner)
        opposite_player = Player.TWO if winner == Player.ONE else Player.ONE

        if current_winner_score == 0:
            self.game_score[winner] = 15
        elif current_winner_score == 15:
            self.game_score[winner] = 30
        elif current_winner_score == 30:
            self.game_score[winner] = 40
        elif current_winner_score == 40:
            opposite_score = game_score[opposite_player]
            if opposite_score < 40:
                # victoire
                # self.game_score[winner] = 0
                self.match_score[winner] += 1
                self.game_score = {Player.ONE: 0, Player.TWO: 0}
                self.score_advantage = {Player.ONE: 0, Player.TWO: 0}
            else:
                score_advantage = self.get_score_advantage()
                if score_advantage[winner] == 1:
                    self.match_score[winner] += 1
                    self.game_score = {Player.ONE: 0, Player.TWO: 0}
                    self.score_advantage = {Player.ONE: 0, Player.TWO: 0}
                elif score_advantage[opposite_score] == 1:
                    self.score_advantage = {Player.ONE: 0, Player.TWO: 0}
                else:
                    self.score_advantage = {Player.ONE: 1, Player.TWO: 0}


    def get_game_score(self):
        return self.game_score

    def get_match_score(self):
        return self.match_score

    def get_score_advantage(self):
        return self.score_advantage

