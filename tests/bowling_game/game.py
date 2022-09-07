import pytest

from src.bowling_game.game import Game

def test_simple_score():
    game = Game()
    game.roll(4)
    assert(game.score == 4)