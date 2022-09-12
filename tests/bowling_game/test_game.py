from src.bowling_game.game import Game

def test_simple_score() -> None:
    game = Game()
    game.roll(5)
    assert(game.score() == 5)
    
def test_two_rolls() -> None:
    game = Game()
    game.roll(4)
    game.roll(6)
    assert(game.score() == 10)

def test_spare() -> None:
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert(game.score() == 16)

def test_invalid_spare() -> None:
    game = Game()
    game.roll(4)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert(game.score() == 17)

def test_strike() -> None:
    game = Game()
    game.roll(10)
    game.roll(5)
    game.roll(3)
    assert(game.score() == 26)

def test_strike_like_spare() -> None:
    game = Game()
    game.roll(0)
    game.roll(10)
    game.roll(3)
    game.roll(2)
    assert(game.score() == 18)
