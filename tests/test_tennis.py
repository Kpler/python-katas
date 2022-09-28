from src.tennis_game.tennis import TennisMatch, Set


def test_get_set_score():
    tennis_set = Set()
    assert tennis_set.get_score() == (0, 0)


def test_get_empty_match_score():
    tennis_game = TennisMatch()
    assert tennis_game.get_score() == []


def test_get_non_empty_match_score():
    tennis_match = TennisMatch()
    tennis_match.add_point(0)
    assert tennis_match.get_score() == [(0, 0), (15, 0)]
