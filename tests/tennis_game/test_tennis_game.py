from src.tennis_game.main import Game

PLAYER_1 = 0
PLAYER_2 = 1


def test_game_is_set():
    game = Game()

    assert game.score() == "love-love"


def test_game_score_updates():
    game = Game()
    game.score_point(PLAYER_1)

    assert game.score() == "15-love"
