from typing import Any, List


class TennisMatch:
    _score: List = []

    def getScore(self) -> List[Any]:
        return self._score


class Set:
    _score_player1: int
    _score_player2: int

    def getScore(self) -> List[Any]:
        return (self._score_player1, self._score_player1)


class Game:
    _score_player1: int
    _score_player1: int

## player1: 6 3 40
## player2: 4 3 30
