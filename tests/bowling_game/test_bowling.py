

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

def test_one_roll() ->  None:
    g = Game()
    g.roll(5)
    assert(g.current_roll == 1)
    assert(g.score == 5)
    assert(g.rolls[0] == 5)
    assert(g.rolls[1:] == [0]*20)

def test_bad_score() ->  None:
    g = Game()
    bad_roll = 3
    for _ in range(20):
        g.roll(bad_roll)
    assert(g.current_roll == 20)
    assert(g.score == 60)
    assert(g.rolls[:-1] == [3]*20)
    assert(g.rolls[-1] == 0)

def test_perfect_score() ->  None:
    g = Game()
    perfect_roll = 10
    for _ in range(10):
        g.roll(perfect_roll)
    assert(g.current_roll == 21)
    assert(g.score == 300)


def test_strike() ->  None:
    """
    frame1: +10
    frame2: +5 , +5
    """
    g = Game()
    perfect_roll = 10
    normal_roll = 5
    # first frame
    g.roll(perfect_roll)
    # second frame
    g.roll(normal_roll)
    g.roll(normal_roll)
    assert(g.current_roll == 4)
    assert(g.score == 30)

def test_two_consecutive_strikes() ->  None:
    """
    frame1: +10
    frame2: +10
    """
    g = Game()
    perfect_roll = 10
    normal_roll = 5
    # first frame
    g.roll(perfect_roll)
    # second frame
    g.roll(perfect_roll) # bonus_frame_1 = 10
    # third frame
    g.roll(normal_roll) # bonus_frame_1 += 5, bonus_frame_2 += 5
    g.roll(normal_roll) # bonus_frame_2 += 5
    assert(g.current_roll == 6)
    assert(g.score == 55)