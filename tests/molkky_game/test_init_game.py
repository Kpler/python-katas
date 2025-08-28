from molkky_game.game import MolkkyGame


def test_init_game():
    game = MolkkyGame()
    assert game.score == 0


def test_score_one_pin():
    game = MolkkyGame()
    game.kick_pins([5])
    assert game.number_pins_down == 1
    assert game.score == 5


def test_score_several_pins():
    game = MolkkyGame()
    game.kick_pins([5, 3, 1])
    assert game.number_pins_down == [5, 3, 1]
    assert game.score == 3
