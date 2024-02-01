from src.molkky_game.molkky_game import MolkkyGame, MolkkyGameState, MolkkyScore, Pin, MAX_SCORE


def test_molkky_game():
    game = MolkkyGame()
    zero_score = MolkkyScore(0)
    assert game.score == zero_score


def test_correct_score_after_one_pin_down():
    game = MolkkyGame()
    game = game.pin_down(frozenset({Pin.ONE}))
    assert game.score == MolkkyScore(1)

    game = game.pin_down(frozenset({Pin.TWO}))
    assert game.score == MolkkyScore(3)


def test_correct_score_when_no_pins_down():
    game = MolkkyGame()
    game = game.pin_down(frozenset())

    assert game.score == MolkkyScore(0)


def test_correct_score_when_two_pins_down():
    game = MolkkyGame()
    game = game.pin_down(frozenset({Pin.FOUR, Pin.FIVE}))

    assert game.score == MolkkyScore(2)


def test_score_fifty():
    game = MolkkyGame()
    for i in range(5):
        game = game.pin_down(frozenset({Pin.ELEVEN}))

    assert game.score == MolkkyScore(25)


def test_should_count_pin_just_once():
    game = MolkkyGame()
    game = game.pin_down(frozenset({Pin.FOUR, Pin.FOUR}))

    assert game.score == MolkkyScore(4)


def test_should_be_won_on_max_score():
    game = MolkkyGame()
    for i in range(5):
        game = game.pin_down(frozenset({Pin.TEN}))

    assert game.state == MolkkyGameState.WON
    assert game.score == MolkkyScore(MAX_SCORE)
