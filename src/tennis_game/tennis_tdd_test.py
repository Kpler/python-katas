import pytest
from dataclasses import dataclass

# implementation here


@dataclass()
class Player:
  score: int = 0
  def get_score(self):
    return self.score


@dataclass()
class Game:
  player_1: Player = Player()
  player_2: Player = Player()
  def increment_score(self, player: Player):
    player.score += 15


# tests here
def test_game_starts_at_zero_zero():
  empty_game = Game()

  assert empty_game.player_1.get_score() == 0, "Player 1 score isn't zero"
  assert empty_game.player_2.get_score() == 0, "Player 2 score isn't zero"


def test_first_point():
  game = Game()
  game.increment_score(game.player_1)
  assert game.player_1.get_score() == 15, "Player 1 score isn't 15"
  assert game.player_2.get_score() == 0, "Player 2 score isn't zero"


