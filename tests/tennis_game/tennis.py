import pytest

from src.tennis_game.tennis import Tennis


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score.get("one") == 0
  assert score.get("two") == 0


def test_play_should_increment_score():
  game = Tennis()

  game.play('one')
  score = game.get_game_score()

  assert score.get("one") == 15
  assert score.get("two") == 0

# def test_game_score_should_reset_at_end_of_game():
#   game = Tennis()

#   game.play('one')
#   game.play('one')
#   game.play('one')
#   game.play('one')
#   score = game.get_game_score()

#   assert score.get("one") == 0
#   assert score.get("two") == 0

def test_game_score_should_increment_after_each_point():
  game = Tennis()

  game.play('one')
  score = game.get_game_score()
  assert score.get("one") == 15

  game.play('one')
  score = game.get_game_score()
  assert score.get("one") == 30

  game.play('one')
  score = game.get_game_score()
  assert score.get("one") == 40
