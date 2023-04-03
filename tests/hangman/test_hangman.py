from src.hangman.hangman import Hangman


def test_guess_found():
    game = Hangman('kata')
    assert game.guess('a') == '_a_a'
    assert game._mistakes_left == 6
    assert game.guess('k') == 'ka_a'



def test_guess_not_found():
    game = Hangman('kata')
    assert game.guess('z') == '____ # z'
    assert game._mistakes_left == 5


def test_mistakes():
    game = Hangman('')
    assert Hangman.MISTAKES_ALLOWED == game._mistakes_left


def test_too_much_mistakes():
    game = Hangman('kata')
    curr = ""
    for _ in range(6):
        curr = game.guess('z')
    assert curr == "The game has ended."
