from hangman.hangman import Hangman

def test_hangman_success():
    h = Hangman("toto")
    result = h.guess("o")
    assert result == "_o_o"
    
def test_hangman_fail():
    h = Hangman("toto")
    result = h.guess("u")
    assert result == "____ # u"

def test_hangman_fail_twice():
    h = Hangman("toto")
    h.guess("u")
    result = h.guess("u")
    assert result == "____ # u"

def test_hangman_successfully_finished():
    h = Hangman("toto")
    h.guess("o")
    result = h.guess("t")
    assert result == "# You found the word! (toto)"
    
def test_hangman_has_ended():
    h = Hangman("toto")
    h.guess("o")
    h.guess("t")
    result = h.guess("t")
    assert result == "# The game has ended"

def test_hangman_is_failed():
    h = Hangman("toto")
    for s in list('abcdef'):
        h.guess(s)
    result = h.guess("g")
    assert result == "# You got hung! The word was toto."


if __name__ == "__main__":
    test_hangman_has_ended()

