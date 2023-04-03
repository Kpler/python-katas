from src.hangman.hangman import Hangman


def test_dummy():
    assert True

def test_guess():
    game = Hangman('kata')
    game.guess('k')
    
    assert True


def test_mistakes():
    game = Hangman('')
    assert game.mistakes == 6