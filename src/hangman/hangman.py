class Hangman:
    MISTAKES_ALLOWED = 6
    HIDE_CHARACTER = '_'

    def __init__(self, word: str):
        self._word = word
        self._mistakes_left = self.MISTAKES_ALLOWED
        self._current_word = self.HIDE_CHARACTER*len(self._word)

    def guess(self, letter: str) -> str:
        if letter in self._word:
            for pos, char in enumerate(self._word):
                if char == letter:
                    self._current_word = self._current_word[:pos] + letter + self._current_word[pos+1:]
            if self._current_word == self._word:
                return f"You found the word! ({self._word})"
            return self._current_word

        else:
            self._mistakes_left -= 1
            if self._mistakes_left <= 0:
                return "The game has ended."
            return self._current_word + ' # ' + letter
