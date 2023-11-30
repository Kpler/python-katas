from src.tennis_game.tennis_game import TennisGame
from src.tennis_game.tennis_game import Player

import pytest


def test_initialise():
    game = TennisGame()
    assert game.score == 'love-love'


def test_score_tennis_game_increasing():
    game = TennisGame()
    game.ball_result(1)
    assert game.score == "15-love"
    game.ball_result(1)
    assert game.score == "30-love"
    game.ball_result(1)
    assert game.score == "40-love"


@pytest.mark.parametrize("player", [1, 2])
def test_player_1_win(player):
    game = TennisGame()
    game.ball_result(player)
    game.ball_result(player)
    game.ball_result(player)
    game.ball_result(player)
    assert game.score == f"Player {player} won"


def _arrive_to_deuce():
    game = TennisGame()
    game.ball_result(1)
    game.ball_result(1)
    game.ball_result(1)
    game.ball_result(2)
    assert game.score == "40-15"
    game.ball_result(2)
    assert game.score == "40-30"
    game.ball_result(2)
    assert game.score == "deuce"
    return game


def test_deuce():
    return _arrive_to_deuce()


def test_advantages():
    game = _arrive_to_deuce()
    game.ball_result(1)
    assert game.score == "advantage player 1"
