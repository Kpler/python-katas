from src.tennis_game.tennis import TennisMatch, Set


def test_get_score():
    tennisGame = TennisMatch()
    assert tennisGame.getScore() == []


def test_get_set_score():
    set = Set()
    assert set.getScore() == []
