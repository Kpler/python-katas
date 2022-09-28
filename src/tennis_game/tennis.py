class Tennis:

    current_player: str
    game_score: dict

    def __init__(self) -> None:
        self.game_score = { 'one': 0, 'two': 0 }

    def play(self, winner: str):
        pass

    def get_score(self):
        return self.game_score