import pytest

from src.tennis_game.tennis import Tennis, Player


def test_initial_score_should_be_zero():
  # given
  game = Tennis()
  score = game.get_game_score()

  # then
  assert score.get(Player.ONE) == 0
  assert score.get(Player.TWO) == 0


def test_play_should_increment_score():
  # given
  game = Tennis()
  one = Player.ONE
  two = Player.TWO

  # when
  game.play(winner=one)
  game_score = game.get_game_score()

  # then
  assert game_score.get(one) == 15
  assert game_score.get(two) == 0


def test_one_play_should_not_increment_match_score():
  # given
  game = Tennis()
  one = Player.ONE
  two = Player.TWO

  # when
  game.play(winner=one)
  match_score = game.get_match_score()

  # then
  assert match_score.get(one) == 0
  assert match_score.get(one) == 0


def test_score_after_two_plays():
  # given
  game = Tennis()
  one = Player.ONE
  two = Player.TWO

  # when
  game.play(winner=one)
  game.play(winner=one)
  game_score = game.get_game_score()

  # then
  assert game_score.get(one) == 30
  assert game_score.get(two) == 0


def test_white_game():
  # given
  game = Tennis()
  one = Player.ONE
  two = Player.TWO

  # when
  game.play(winner=one)
  game.play(winner=one)
  game.play(winner=one)
  game.play(winner=one)
  game_score = game.get_game_score()

  # then
  assert game_score.get(one) == 0
  assert game_score.get(two) == 0


def test_player_two_does_not_keep_points_after_losing():
  # given
  game = Tennis()
  one = Player.ONE
  two = Player.TWO

  # when
  game.play(winner=one)
  game.play(winner=two)
  game.play(winner=one)
  game.play(winner=one)
  game.play(winner=one)
  game_score = game.get_game_score()
  match_score = game.get_match_score()

  # then
  assert game_score.get(one) == 0
  assert game_score.get(two) == 0
  assert match_score.get(one) == 1
  assert match_score.get(two) == 0



