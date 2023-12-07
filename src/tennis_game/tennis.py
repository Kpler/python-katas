
points = ["love", "15", "30", "40"]

class WrongPlayerException(Exception):
    pass

class TennisGame:

    def __init__(self):
        self.players_scores: dict[int, int] = {
            1: 0,
            2: 0,
        }

    def get_score(self) -> str:
        if self._get_potential_deuce():
            return "deuce"
        potential_winner = self._get_potential_winner()
        if potential_winner:
            return f"Player {potential_winner} Win!"
        return f"{points[self.players_scores[1]]} - {points[self.players_scores[2]]}"

    def gain_point(self, player: int) -> None:
        if player not in [1,2]:
            raise WrongPlayerException()
        self.players_scores[player] += 1

    def _get_potential_winner(self) -> int | None:
        if self.players_scores[1] >= 4:
            return 1
        if self.players_scores[2] >= 4:
            return 2

    def _get_potential_deuce(self) -> bool:
        return self.players_scores[1] >= 3 and self.players_scores[1] == self.players_scores[2]
