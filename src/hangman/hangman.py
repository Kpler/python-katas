class Hangman:
    def __init__(self, word):
        self.word = word
        self.status = "ongoing"
        # self.current_guesses = ''.join(['_' * len(word)])
        self.right_guesses = ""
        self.wrong_guesses = ""

    def guess(self, letter):
        if letter in self.word:
            self.right_guesses += letter
        else:
            self.wrong_guesses += letter

        current_result = "".join([l if l in self.right_guesses else "_" for l in self.word])
        if self.wrong_guesses:
            current_result += f" # {self.wrong_guesses}"
        return current_result

