import pytest

from src.tennis_game.tennis import Tennis, Player, Score


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score.get(Player.ONE) == Score.LOVE
  assert score.get(Player.TWO) == Score.LOVE


def test_play_should_increment_score():
  game = Tennis()

  game.play(Player.ONE)
  score = game.get_game_score()

  assert score.get(Player.ONE) == Score.FIFTEEN
  assert score.get(Player.TWO) == Score.LOVE


def test_game_score_should_increment_after_each_point():
  game = Tennis()

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == Score.FIFTEEN

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == Score.THIRTY

  game.play(Player.ONE)
  score = game.get_game_score()
  assert score.get(Player.ONE) == Score.FORTY


def test_game_score_should_reset_at_end_of_game():
  game = Tennis()

  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.ONE)
  score = game.get_game_score()
  match_score = game.get_match_score()

  assert score.get(Player.ONE) == Score.LOVE
  assert score.get(Player.TWO) == Score.LOVE
  assert match_score == { Player.ONE: 1, Player.TWO: 0 }

def test_game_should_continue_if_deuce():
  game = Tennis()

  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.ONE)
  game.play(Player.TWO)
  game.play(Player.TWO)
  game.play(Player.TWO)

  game.play(Player.ONE)
  score = game.get_game_score()
  match_score = game.get_match_score()

  assert score.get(Player.ONE) == Score.ADVANTAGE
  assert score.get(Player.TWO) == Score.FORTY
  # assert match_score == { Player.ONE: 1, Player.TWO: 0 }