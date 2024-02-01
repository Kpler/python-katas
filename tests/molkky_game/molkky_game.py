from src.molkky_game.molkky_game import MolkkyGame, MolkkyScore, Pin


def test_molkky_game():
    game = MolkkyGame()
    zero_score = MolkkyScore(0)
    assert game.score == zero_score


def test_correct_score_after_one_pin_down():
    game = MolkkyGame()
    game = game.pin_down([Pin.ONE])
    assert game.score == MolkkyScore(1)

    game = game.pin_down([Pin.TWO])
    assert game.score == MolkkyScore(3)


def test_correct_score_when_no_pins_down():
    game = MolkkyGame()
    game = game.pin_down([])

    assert game.score == MolkkyScore(0)


def test_correct_score_when_two_pins_down():
    game = MolkkyGame()
    game = game.pin_down([Pin.FOUR, Pin.FIVE])

    assert game.score == MolkkyScore(2)

def test_score_fifty():
    game = MolkkyGame()
    for i in range(5):
        game = game.pin_down([Pin.ELEVEN])
        
    assert game.score == MolkkyScore(25)
