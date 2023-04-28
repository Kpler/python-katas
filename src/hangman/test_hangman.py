import pytest

from hangman import Hangman


def test_fails_on_letter_not_present_and_displays_the_letter():
    hangman = Hangman("word")
    result = hangman.guess("z")
    assert result == "_ _ _ _ # z"


def test_fails_on_another_missing_letter():
    hangman = Hangman("word")
    result = hangman.guess("z")
    result = hangman.guess("t")
    assert result == "_ _ _ _ # zt"


def test_successes_with_a_present_letter():
    hangman = Hangman("word")
    result = hangman.guess("w")
    assert result == "w _ _ _"


def test_guess_same_letter_twice():
    hangman = Hangman("word")
    result = hangman.guess("w")
    assert result == "w _ _ _"
    result = hangman.guess("w")
    assert result == "w _ _ _"
    result = hangman.guess("z")
    assert result == "w _ _ _ # z"
    result = hangman.guess("z")
    assert result == "w _ _ _ # z"


def test_successes_with_a_second_present_letter():
    hangman = Hangman("word")
    hangman.guess("w")
    assert hangman.guess("o") == "w o _ _"

def test_keep_first_failure():
    word = "word"
    hangman = Hangman(word)
    hangman.guess("w")
    hangman.guess("z")
    result = hangman.guess("o")
    assert result == "w o _ _ # z"


def test_keep_all_failures():
    word = "word"
    hangman = Hangman(word)
    hangman.guess("w")
    hangman.guess("z")
    result = hangman.guess("y")
    assert result == "w _ _ _ # zy"


def test_win_game():
    word = "word"
    hangman = Hangman(word)
    hangman.guess("w")
    hangman.guess("z")
    result1 = hangman.guess("o")
    assert result1 == "w o _ _ # z"
    hangman.guess("r")
    result2 = hangman.guess("d")
    expected = f"You found the word! ({word})"
    assert result2 == expected
    result3 = hangman.guess("g")
    assert result3 == "The game has ended."

def test_lose_game():
    word = "word"
    hangman = Hangman(word)
    hangman.guess("y")
    hangman.guess("z")
    hangman.guess("a")
    hangman.guess("b")
    hangman.guess("c")
    hangman.guess("d")
    result = hangman.guess("e")
    assert result == f"You got hung! The word was {word}."
