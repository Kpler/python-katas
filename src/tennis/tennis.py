from enum import Enum


class WinningGame(Exception):
    pass


class Player(Enum):
    ONE = (0,)
    TWO = (1,)


class Tennis:
    _score_map = {0: "love", 1: "15", 2: "30", 3: "40"}

    def __init__(self) -> None:
        self._scores = (0, 0)

    def _update_score(self, player: Player) -> None:
        (score_1, score_2) = self._scores
        if player == Player.ONE:
            self._scores = (score_1 + 1, score_2)
        elif player == Player.TWO:
            self._scores = (score_1, score_2 + 1)
        else:
            raise NotImplementedError()

    def _print_score(self) -> str:
        (score_1, score_2) = self._scores
        if score_1 >= 3 and score_2 >= 3:
            if score_1 == score_2:
                return "deuce"
            if score_1 > score_2:
                return "advantage one"
            return "advantage two"

        player_1_score = self._score_map[score_1]
        player_2_score = self._score_map[score_2]
        return f"{player_1_score}-{player_2_score}"

    def _check_win(self) -> None:
        (score_1, score_2) = self._scores
        if (score_1 >= 4 or score_2 >= 4) and abs(score_1 - score_2) > 1:
            raise WinningGame()

    def play(self, player: Player) -> str:
        self._update_score(player)
        self._check_win()
        return self._print_score()
