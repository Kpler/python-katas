class Player:

    def __init__(self):
        self.score=0
        
    def set_score(self, new_score: str) -> None:
        self.score=new_score



class Game:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        pass

    def score(self) -> str:
        return "0 - 0"

    def play(self, winner: int) -> int:
        self.player_1.set_score()
