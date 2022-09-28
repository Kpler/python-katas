import pytest

from src.tennis_game.main import Game

PLAYER_1 = 0
PLAYER_2 = 1


def test_game_is_set():
    game = Game()

    assert game.score() == "love-love"


def test_game_score_updates():
    game = Game()
    game.score_point(PLAYER_1)

    assert game.score() == "15-love"


def test_game_win_player_1():
    game = Game()
    game.score_point(PLAYER_1)
    game.score_point(PLAYER_1)
    game.score_point(PLAYER_2)
    game.score_point(PLAYER_1)

    with pytest.raises(Exception):
        game.score_point(PLAYER_1)


def _deuce_situation(game):
    """ Go to 40-40 """

    game.score_point(PLAYER_1)
    game.score_point(PLAYER_2)
    game.score_point(PLAYER_1)
    game.score_point(PLAYER_2)
    game.score_point(PLAYER_2)
    game.score_point(PLAYER_1)


def test_game_deuce():
    game = Game()
    _deuce_situation(game)

    assert game.score() == "deuce"


def test_game_advantage_after_deuce():
    game = Game()
    _deuce_situation(game)
    game.score_point(PLAYER_1)

    assert game.score() == "adv-40"


def test_game_win_after_deuce():
    game = Game()
    _deuce_situation(game)
    game.score_point(PLAYER_1)

    with pytest.raises(Exception):
        game.score_point(PLAYER_1)


def test_game_deuce_after_deuce():
    game = Game()
    _deuce_situation(game)
    game.score_point(PLAYER_1)
    game.score_point(PLAYER_2)

    assert game.score() == "deuce"
