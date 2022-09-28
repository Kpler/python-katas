from typing import Any, List, Tuple


class Game:
    _score_player1: int = 0
    _score_player2: int = 0


class Set:
    _score_player1: int
    _score_player2: int
    _ongoing_game: Game = Game()

    def __init__(self, score_p_1: int = 0, score_p_2: int = 0):
        self._score_player1 = score_p_1
        self._score_player2 = score_p_2

    def getScore(self) -> Tuple[int, int]:
        return self._score_player1, self._score_player1


class TennisMatch:
    _score: List[Set] = []

    def getScore(self) -> List[Any]:
        return self._score



## player1: 6 3 40
## player2: 4 3 30

