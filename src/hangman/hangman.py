class Hangman:
    def __init__(self, word):
        self.word = word
        self.status = "ongoing"
        self.current_guesses = ''.join(['_' * len(word)])
        self.wrong_guesses = []

    def guess(self, letter):
        # TODO
        guessed_word = self.current_guesses
        return guessed_word

