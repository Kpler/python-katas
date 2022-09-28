from src.tennis_game.tennis import TennisGame


def test_get_score():
    tennisGame = TennisGame()
    assert tennisGame.getScore() is None
