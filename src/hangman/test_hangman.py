import pytest


class Hangman:

    def __init__(self, word):
        self.word_to_guess = word
        self.previous_miss = None
        self.status = "_ " * len(word)

    def guess(self, letter):
        if letter not in self.word_to_guess:
            self.previous_miss = letter
        postfix = f"# {self.previous_miss}" if self.previous_miss else ""
        if letter in self.word_to_guess:
            letter_index = self.word_to_guess.index(letter)
            self.status[letter_index * 2] = letter
        return f'{self.status}{postfix}'


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
