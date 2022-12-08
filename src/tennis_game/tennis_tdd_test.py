import pytest
from dataclasses import dataclass

# implementation here
@dataclass()
class Game():
  player_1_score: int = 0
  player_2_score: int = 0


# tests here
def test_game_starts_at_zero_zero():

  empty_game = Game()

  assert empty_game.player_1_score == 0, "Player 1 score isn't zero"
  assert empty_game.player_2_score == 0, "Player 2 score isn't zero"


