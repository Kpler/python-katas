from typing import Literal

points = ["love", "15", "30", "40", "win"]

class IllegalPlayerException(Exception):
    pass

class TennisGame:
    score_player_1: int = 0
    score_player_2: int = 0
    score = ["love", "love"]
    status: Literal["start", "on_going", "finished"] = "start"

    def play(self, scorer: int) -> None:
        if scorer not in [1, 2]:
            raise IllegalPlayerException(f"{scorer} is not a accepted player")
        if scorer == 1:
            self.score_player_1 += 1
        else:
            self.score_player_2 += 1


    def get_score(self) -> str:
        if (self.score_player_2 == self.score_player_1) and self.score_player_1 >= 3:
            return "deuce"
        return f"{points[self.score_player_1]} - {points[self.score_player_2]}"
