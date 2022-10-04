from enum import Enum


class SCORES (Enum):
  LOVE = 0
  FIFTEEN = 15
  THIRTY = 30
  FORTY = 40

class Tennis:
  score_player_1 = SCORES.LOVE
  score_player_2 = SCORES.LOVE
  def get_game_score(self):
    return f"{self.score_player_1.value}-{self.score_player_2.value}"

  def play(self, player: str):
    if player == "0" and self.score_player_1 == SCORES.LOVE:
      self.score_player_1 = SCORES.FIFTEEN
    elif player == "0" and self.score_player_1 == SCORES.FIFTEEN:
      self.score_player_1 = SCORES.THIRTY
    elif player == "0" and self.score_player_1 == SCORES.THIRTY:
      self.score_player_1 = SCORES.FORTY
    elif player == "1" and self.score_player_2 == SCORES.LOVE:
      self.score_player_2 = SCORES.FIFTEEN
    elif player == "1" and self.score_player_2 == SCORES.FIFTEEN:
      self.score_player_2 = SCORES.THIRTY
    elif player == "1" and self.score_player_2 == SCORES.THIRTY:
      self.score_player_2 = SCORES.FORTY
