from molkky_game.game import MolkkyGame


def test_init_game():
    game = MolkkyGame()
    assert game.score == 0


def test_score_one_pin():
    game = MolkkyGame()
    game.kick_pins([5])
    assert game.pins_down == [5]
    assert game.score == 5


def test_score_several_pins():
    game = MolkkyGame()
    game.kick_pins([5, 3, 1])
    assert game.pins_down == [5, 3, 1]
    assert game.score == 3


def test_score_exceed_rest_to_25():
    game = MolkkyGame()
    game.score = 47
    game.kick_pins([7])
    assert game.score == 25

def test_win_game():
    game = MolkkyGame()
    game.score = 47
    game.kick_pins([3])
    assert game.score == 50
    assert game.status == "win"

def test_loose_game():
    game = MolkkyGame()
    game.score = 47
    game.kick_pins([])
    game.kick_pins([])
    game.kick_pins([])
    assert game.status == "lost"

def test_successive_failed_attempts():
    game = MolkkyGame()
    game.score = 40
    game.kick_pins([])
    game.kick_pins([])
    game.kick_pins([3])
    game.kick_pins([])
    assert game.status == "ongoing"
    assert game.failed_attempts == 1