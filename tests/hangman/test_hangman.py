from hangman.hangman import Hangman
def test_hangman_success():
    h = Hangman("toto")
    h.guess("o")
    print(h.prompt)
    assert h.prompt == "_o_o"
    
def test_hangman_fail():
    h = Hangman("toto")
    h.guess("u")
    print(h.prompt)
    assert h.prompt == "____" 
    
    
if __name__ == "__main__":
    test_hangman_success()

