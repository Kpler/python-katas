from molkky_game.game import MolkkyGame

def test_init_game():
    game = MolkkyGame()
    assert game.score == 0
