from src.tennis_game.tennis import TennisMatch, Set


def test_get_set_score():
    tennis_set = Set()
    assert tennis_set.getScore() == (0, 0)


def test_get_empty_match_score():
    tennisGame = TennisMatch()
    assert tennisGame.getScore() == []


def test_get_non_empty_match_score():
    tennisGame = TennisMatch()
    tennisSet = Set(3, 2)
    tennisGame._score.append(tennisSet)
    assert tennisGame.getScore() == [(3, 2)]
