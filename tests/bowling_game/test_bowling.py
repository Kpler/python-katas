from bowling_game.bowling import Game


def test_roll_nothing():
    game = Game()

    game.roll(0)

    assert game.score() == 0

def test_roll_one():
    game = Game()

    game.roll(1)

    assert game.score() == 1


def test_several_rolls():
    game = Game() 

    game.roll(1)
    game.roll(4)

    assert game.score() == 5