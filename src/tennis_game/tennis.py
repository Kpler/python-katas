class Player:

    def __init__(self):
        self.score = 0
        
    def set_score(self, new_score: int) -> None:
        self.score = new_score


class Game:
    player_1_score: int = 0
    player_2_score: int = 0

    def score(self) -> str:
        if self.player_1_score == self.player_2_score:
            return "0 - 0"
        return "15 - 0"

    def play(self, winner: int) -> None:
        self.player_1_score = 1
