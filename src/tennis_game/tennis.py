from typing import Any, List, Tuple


class Game:
    _score_player1: int = 0
    _score_player2: int = 0

    def get_score(self) -> Tuple[int, int]:
        return self._score_player1, self._score_player2

    def add_point(self, p):
        if p == 0:
            self._score_player1 = 15
        else:
            self._score_player2 = 15


class Set:
    _score_player1: int
    _score_player2: int

    def __init__(self, score_p_1: int = 0, score_p_2: int = 0):
        self._score_player1 = score_p_1
        self._score_player2 = score_p_2

    def get_score(self) -> Tuple[int, int]:
        return self._score_player1, self._score_player1


class TennisMatch:
    _set_score: List[Set] = []
    _ongoing_game: Game = Game()

    def add_point(self, p: int):
        self._ongoing_game.add_point(p)

    def get_score(self) -> List[Tuple[int, int]]:
        set_scores = [s.get_score() for s in self._set_score]
        if len(set_scores) == 0:
            set_scores = [(0, 0)]
        set_scores.append(self._ongoing_game.get_score())
        return set_scores



## player1: 6 3 40
## player2: 4 3 30

# p1 gagne un point (0,0 -> 0 15)
# p2 gagne un point (0,0 -> 15 15)
