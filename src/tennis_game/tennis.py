class Tennis:

    current_player: str
    game_score: dict

    def __init__(self) -> None:
        self.game_score = { "one": 0, "two": 0 }

    def play(self, winner: str): # TODO one/two
        current_winner_score = self.game_score.get(winner)

        if current_winner_score == 0:
            self.game_score[winner] = 15


    def get_score(self):
        return self.game_score
