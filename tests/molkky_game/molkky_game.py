from src.molkky_game.molkky_game import MolkkyGame, MolkkyScore


def test_molkky_game():
    game = MolkkyGame()
    zero_score = MolkkyScore(0)
    assert game.score == zero_score


def test_correct_score_after_one_pin_down():
    game = MolkkyGame()
    game = game.pin_down([1])
    assert game.score == MolkkyScore(1)

    game = game.pin_down([2])
    assert game.score == MolkkyScore(3)


def test_correct_score_when_no_pins_down():
    game = MolkkyGame()
    game = game.pin_down([])

    assert game.score == MolkkyScore(0)


def test_correct_score_when_two_pins_down():
    game = MolkkyGame()
    game = game.pin_down([4, 5])

    assert game.score == MolkkyScore(2)
