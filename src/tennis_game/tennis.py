from typing import Sequence


class Game:

    player_1_score: int = 0
    player_2_score: int = 0
    score_labels: Sequence[str] = ("love", "15", "30", "40")

    def __int__(self):
        pass

    def player_1_scored(self) -> None:
        self.player_1_score += 1

    def player_2_scored(self) -> None:
        self.player_2_score += 1

    def is_finished(self) -> bool:
        return self.player_1_score > 3 or self.player_2_score > 3


    def get_score(self) -> str:
        if self.is_finished():
            return "Player 1 wins" if self.player_1_score > 3 else "Player 2 wins"
        return f"{self.score_labels[self.player_1_score]}-{self.score_labels[self.player_2_score]}"
