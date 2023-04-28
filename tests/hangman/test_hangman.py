from src.hangman.hangman import Hangman


def test_create_hangman():
    hangman = Hangman("word")
    assert hangman

    assert hangman.guess("w") == "w _ _ _"
    assert hangman.guess("o") == "w o _ _"
    assert hangman.guess("r") == "w o r _"


def test_number_of_mistakes():
    hangman = Hangman("word")
    assert hangman.number_of_mistakes == 0
    hangman.guess("a")
    assert hangman.number_of_mistakes == 1

def test_game_over():
    hangman = Hangman("word")
    hangman.guess("a")
    hangman.guess("a")
    hangman.guess("a")
    hangman.guess("a")
    hangman.guess("a")
    assert hangman.guess("a") == "Game over"


