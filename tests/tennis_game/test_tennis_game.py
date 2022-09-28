from src.tennis_game.main import Game


def test_game_is_set():
    game = Game()

    assert game.score() == "love-love"


def test_game_score_updates():
    game = Game()
    game.score_point(0)

    assert game.score() == "15-love"

