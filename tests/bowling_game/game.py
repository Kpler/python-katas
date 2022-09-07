import pytest

from src.bowling_game.game import Game

def test_simple_score():
    game = Game()
    game.roll(4)
    assert(game.score == 4)
    
def test_two_rolls():
    game = Game()
    game.roll(4)
    game.roll(6)
    assert(game.score == 10)