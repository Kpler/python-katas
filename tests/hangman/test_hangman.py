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


def test_guess_wrong():
    hangman = Hangman(
        word="hangman"
    )
    test_guess = hangman.guess(letter="w")
    assert test_guess == "_______ # w"
    assert hangman.status == "ongoing"


def test_guess_wrong():
    hangman = Hangman(
        word="hangman"
    )
    test_guess = hangman.guess(letter="h")
    test_guess = hangman.guess(letter="a")
    test_guess = hangman.guess(letter="n")
    test_guess = hangman.guess(letter="g")
    test_guess = hangman.guess(letter="m")
    assert test_guess == f"You found the word! (\"hangman\")"
