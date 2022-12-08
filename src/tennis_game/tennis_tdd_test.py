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
    print('CALLED INCREMENT SCORE')
    player.score += 15


# tests here
def test_game_starts_at_zero_zero():
  empty_game = Game()

  assert empty_game.player_1.get_score() == 0, "Player 1 score isn't zero"
  assert empty_game.player_2.get_score() == 0, "Player 2 score isn't zero"


def test_player_1_scores_first_point():
  game = Game()
  game.increment_score(game.player_1)
  assert game.player_1.get_score() == 15, "Player 1 score isn't 15"
  assert game.player_2.get_score() == 0, "Player 2 score isn't zero"


def test_player_1_scores_second_point():
  game2 = Game()
  # print(game2.player_1.get_score())
  game2.increment_score(game2.player_1)
  # print(game2.player_1.get_score())
  game2.increment_score(game2.player_1)
  # print(game2.player_1.get_score())
  assert game2.player_1.get_score() == 30, "Player 1 score isn't 30"
  assert game2.player_2.get_score() == 0, "Player 2 score isn't zero"

