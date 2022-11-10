import pytest

from src.tennis_game.tennis import Tennis, Player


def test_initial_score_should_be_zero():
    game = Tennis()
    score = game.get_game_score()
    assert score.get(Player.ONE) == 0
    assert score.get(Player.TWO) == 0


def test_play_should_increment_game_score_once():
    game = Tennis()
    game.play(Player.ONE)

    score = game.get_game_score()
    assert score.get(Player.ONE) == 15


def test_play_should_increment_game_score_twice():
    game = Tennis()
    game.play(Player.TWO)
    game.play(Player.TWO)

    score = game.get_game_score()
    assert score.get(Player.TWO) == 30


def test_play_should_increment_game_score_three_times():
    game = Tennis()
    game.play(Player.ONE)
    game.play(Player.ONE)
    game.play(Player.ONE)

    score = game.get_game_score()
    assert score.get(Player.ONE) == 40


def test_play_should_increment_match_score():
    game = Tennis()
    game.play(Player.ONE)
    game.play(Player.ONE)
    game.play(Player.ONE)
    game.play(Player.ONE)

    match_score = game.get_match_score()
    game_score = game.get_game_score()
    assert match_score.get(Player.ONE) == 1
    assert match_score.get(Player.TWO) == 0
    assert game_score.get(Player.ONE) == 0
    assert game_score.get(Player.TWO) == 0

