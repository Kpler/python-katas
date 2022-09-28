import pytest

from src.tennis_game.tennis import Tennis


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_score()
  assert score.get("one") == 0
  assert score.get("two") == 0


def test_play_should_increment_score():
  game = Tennis()

  game.play('one')
  score = game.get_score()

  assert score.get("one") == 15
  assert score.get("two") == 0

  

