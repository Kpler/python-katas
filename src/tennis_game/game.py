points = ["love", "15", "30", "40", "advantage", "win"]
class Game:

    def __init__(self):
        self.player1_score_index = 0
        self.player2_score_index = 0
        return

    def start(self) -> None:
        self.nb_players = 2
    
    def player_1_scores(self) -> None:
        self.player1_score_index += 1

    def player_2_scores(self) -> None:
        self.player2_score_index += 1
    
    @property
    def score(self):
        return f"{self.get_player1_score()}-{self.get_player2_score()}"

    def get_player1_score(self) -> str:
        return f"{points[self.player1_score_index]}"

    def get_player2_score(self) -> str:
        return f"{points[self.player2_score_index]}"