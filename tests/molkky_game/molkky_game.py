from src.molkky_game.molkky_game import MolkkyGame, MolkkyScore


def test_molkky_game():
    game = MolkkyGame()
    zero_score = MolkkyScore(0)
    assert game.score == zero_score

    game = game.pin_down(1)
    assert game.score == MolkkyScore(1)

    game = game.pin_down(2)
    assert game.score == MolkkyScore(3)
