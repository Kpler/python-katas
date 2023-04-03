class Hangman:
    def __init__(self, word, max_wrong_guesses=6):
        self.word = word
        self.status = "ongoing"
        # self.current_guesses = ''.join(['_' * len(word)])
        self.right_guesses = ""
        self.wrong_guesses = ""
        self.max_wrong_guesses = max_wrong_guesses

    def guess(self, letter):
        if letter in self.word:
            self.right_guesses += letter
        else:
            self.wrong_guesses += letter

        current_result = "".join([l if l in self.right_guesses else "_" for l in self.word])
        if self.wrong_guesses:
            current_result += f" # {self.wrong_guesses}"

        if current_result == self.word:
            current_result = f"You found the word! (\"{self.word}\")"
            self.status = "won"
        elif len(self.wrong_guesses) == self.max_wrong_guesses:
            current_result = f"You lost! (\"hangman\")"
        return current_result
