from src.tennis_game.tennis import TennisMatch, Set


def test_get_set_score():
    tennis_set = Set()
    assert tennis_set.getScore() == (0, 0)


def test_get_empty_match_score():
    tennisGame = TennisMatch()
    assert tennisGame.getScore() == []


def test_get_non_empty_match_score():
    tennisMatch = TennisMatch()
    tennisMatch.addPoint(0)
    assert tennisGame.getScore() == [(0, 0), (15, 0)]
