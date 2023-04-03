from src.hangman.hangman import Hangman


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


def test_win_status():
    hangman = Hangman(
        word="hangman"
    )
    _ = hangman.guess(letter="h")
    _ = hangman.guess(letter="a")
    _ = hangman.guess(letter="n")
    _ = hangman.guess(letter="g")
    test_guess = hangman.guess(letter="m")
    assert test_guess == f"You found the word! (\"hangman\")"

def test_lose_status():
    hangman = Hangman(
        word="hangman",
        max_wrong_guesses=1
    )
    # TODO: fix this
    test_guess = hangman.guess(letter="z")
    test_guess = hangman.guess(letter="j")
    assert test_guess == f"You lost! (\"hangman\")"
