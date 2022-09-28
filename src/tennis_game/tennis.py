from typing import Any, List, Tuple


class Game:
    _score_player1: int = 0
    _score_player2: int = 0


class Set:
    _score_player1: int
    _score_player2: int

    def __init__(self, score_p_1: int = 0, score_p_2: int = 0):
        self._score_player1 = score_p_1
        self._score_player2 = score_p_2

    def getScore(self) -> Tuple[int, int]:
        return self._score_player1, self._score_player1


class TennisMatch:
    _set_score: List[Set] = []
    _ongoing_game: Game = Game()

    def addPoint(self, p: int):
        self._ongoing_game.addPoint(p)

    def getScore(self) -> [List[Set],[int, int]]:
        return self._set_score,  self._ongoing_game.getScore()



## player1: 6 3 40
## player2: 4 3 30

# p1 gagne un point (0,0 -> 0 15)
# p2 gagne un point (0,0 -> 15 15)
