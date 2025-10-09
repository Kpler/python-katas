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


def test_strike_roll():
    game = Game()
    game.roll(10)

    assert game.score() == 10

    game.roll(3)
    game.roll(5)

    assert game.score() == 26
