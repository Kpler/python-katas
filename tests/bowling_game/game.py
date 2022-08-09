import pytest as pytest

from src.bowling_game.game import Game


def test_all_gutters_should_score_zero():
    game = Game()

    for i in range(0, 21):
        game.roll(0)
    final_score = game.score()

    assert final_score == 0


def test_basic_game_should_add_up_pins():
    game = Game()

    for i in range(0, 20):
        game.roll(1)
    final_score = game.score()

    assert final_score == 20


def test_exceed():
    game = Game()
    with pytest.raises(Exception):
        game.roll(11)
    