from src.hangman.hangman import Hangman


def test_dummy():
    assert True

def test_guess_found():
    game = Hangman('kata')
    curr = game.guess('k')

    assert curr == 'k___'

def test_guess_not_found():
    game = Hangman('kata')
    curr = game.guess('z')

    assert curr == '____'

def test_mistakes():
    game = Hangman('')
    assert Hangman.MISTAKES_ALLOWED == game.mistakes_left
