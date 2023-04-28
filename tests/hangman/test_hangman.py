from src.hangman.hangman import Hangman


def test_create_hangman():
    hangman = Hangman("word")
    assert hangman

    assert hangman.guess("w") == "w _ _ _"
    assert hangman.guess("o") == "w o _ _"

