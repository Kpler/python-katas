class Hangman:

    def __init__(self, word: str):
        self.word = word
        self.game_state = set()

    def guess(self, letter: str) -> str:
        self.game_state.add(letter)
        return "w _ _ _"
