import pytest


class Hangman:

    def __init__(self, word):
        pass

    def guess(self, letter):
        return f'_ _ _ _ # {letter}'


def test_fails_on_letter_not_present_and_displays_the_letter():
    hangman = Hangman("word")
    result = hangman.guess("z")
    assert result == "_ _ _ _ # z"

def test_fails_on_another_missing_letter():
    hangman = Hangman("word")
    result = hangman.guess("t")
    assert result == "_ _ _ _ # t"