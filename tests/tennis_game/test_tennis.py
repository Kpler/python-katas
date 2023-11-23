from src.tennis_game.tennis import Game, Player


def test_tennis():
    p1 = Player()
    p2 = Player()
    game = Game(p1, p2)

    score = game.score()

    assert p1.score() == 0
    assert score == "0 - 0"
