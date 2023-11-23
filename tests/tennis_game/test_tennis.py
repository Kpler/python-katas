from src.tennis_game.tennis import Game


def test_tennis():
    game=Game()
    score=game.score()
    assert score == "0 - 0"

