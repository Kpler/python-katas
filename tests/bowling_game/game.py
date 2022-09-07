from src.bowling_game.game import Game

def test_simple_score():
    game = Game()
    game.roll(5)
    assert(game.score() == 5)
    
def test_two_rolls():
    game = Game()
    game.roll(4)
    game.roll(6)
    assert(game.score() == 10)

def test_spare():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert(game.score() == 16)

def test_invalid_spare():
    game = Game()
    game.roll(4)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert(game.score() == 17)