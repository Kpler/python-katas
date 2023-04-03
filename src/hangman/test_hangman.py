import pytest


class Hangman:

    def __init__(self, word):
        diplay = "_ _ _ _"

    def guess(self, letter):
        if letter == "w":
            return "w _ _ _"
        else:
            return f'_ _ _ _ # {letter}'


def test_fails_on_letter_not_present_and_displays_the_letter():
    hangman = Hangman("word")
    result = hangman.guess("z")
    assert result == "_ _ _ _ # z"


def test_fails_on_another_missing_letter():
    hangman = Hangman("word")
    result = hangman.guess("t")
    assert result == "_ _ _ _ # t"


def test_successes_with_a_present_letter():
    hangman = Hangman("word")
    result = hangman.guess("w")
    assert result == "w _ _ _"


def test_successes_with_a_second_present_letter():
    hangman = Hangman("word")
    hangman.guess("w")
    assert hangman.guess("o") == "w o _ _"