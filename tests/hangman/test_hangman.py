from src.hangman.hangman import Hangman

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


if __name__ == "__main__":
    test_hangman_success()

