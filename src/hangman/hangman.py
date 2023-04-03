class Hangman:
    MISTAKES_ALLOWED = 6

    def __init__(self, word: str):
        self._word = word
        self._mistakes_left = self.MISTAKES_ALLOWED
        self._current_word = '____'

    def guess(self, letter: str) -> str:
        if letter in self._word:
            #indexes = 
            return "k___"
        else:
            self._mistakes_left -= 1
            if self._mistakes_left <= 0:
                return "The game has ended."
            return self._current_word + ' # z'
