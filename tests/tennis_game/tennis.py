import pytest

from src.tennis_game.tennis import Tennis, Player


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score.get(Player.ONE) == 0
  assert score.get(Player.TWO) == 0


def test_play_should_increment_score():
  pass

