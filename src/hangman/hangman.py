class Hangman:
    MISTAKES_DEFAULT = 6

    def __init__(self, word: str):
        self.word = word
        self.mistakes = self.MISTAKES_DEFAULT

    def guess(self, letter: str) -> str:
        pass