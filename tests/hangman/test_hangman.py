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
    hangman.guess(letter="a")
    assert hangman.word == "__a__a_"
    assert hangman.status == "ongoing"
