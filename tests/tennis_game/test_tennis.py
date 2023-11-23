from src.tennis_game.tennis import Game, Player


def test_new_game():
    game = Game()
    score = game.score()
    assert score == "0 - 0"


def test_ongoing_game():
    game = Game()
    game.play(winner=1)
    assert game.score() == "15 - 0"


def test_game_winner():
    game = Game()
    game.play(winner=1)
    game.play(winner=1)
    game.play(winner=1)
    game.play(winner=1)
    assert game.score() == "Player 1 Won"
