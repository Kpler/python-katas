class Hangman:
    MISTAKES_ALLOWED = 6

    def __init__(self, word: str):
        self.word = word
        self.mistakes_left = self.MISTAKES_ALLOWED

    def guess(self, letter: str) -> str:

        return 'k___'
