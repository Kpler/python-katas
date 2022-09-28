import pytest

from src.tennis_game.tennis import Tennis, Player


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score.get(Player.ONE) == 0
  assert score.get(Player.TWO) == 0


def test_play_should_increment_score():
  game = Tennis()

  game.play(Player.ONE)
  score = game.get_game_score()

  assert score.get(Player.ONE) == 15
  assert score.get(Player.TWO) == 0


def test_game_score_should_increment_after_each_point():
  game = Tennis()

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == 15

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == 30

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == 40


def test_game_score_should_reset_at_end_of_game():
  game = Tennis()

  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.ONE)
  score = game.get_game_score()
  match_score = game.get_match_score()

  assert score.get(Player.ONE) == 0
  assert score.get(Player.TWO) == 0
  assert match_score == { Player.ONE: 1, Player.TWO: 0 }