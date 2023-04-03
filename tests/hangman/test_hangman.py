from src.hangman.hangman import Hangman

"""
TODO: implement test for state machine
ongoing
loss
victory
ended
"""


def test_initialisation():
    hangman = Hangman(
        word="hangman",
    )
    assert hangman.word == "hangman"


def test_guess():
    hangman = Hangman(
        word="hangman"
    )
    test_guess = hangman.guess(letter="a")
    assert test_guess == "_a___a_"
    assert hangman.status == "ongoing"
