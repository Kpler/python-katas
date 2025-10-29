

import pytest
from src.bowling_game.bowling import Game

def test_initialize_bowling_game() -> None:
    g = Game()
    assert(g.current_roll == 0)
    assert(g.score == 0)
    assert(g.rolls == [0]*21)

def test_bad_player() ->  None:
    g = Game()
    g.roll(0)
    assert(g.current_roll == 1)
    assert(g.score == 0)
    assert(g.rolls == [0]*21)