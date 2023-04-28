class Hangman:

    def __init__(self, word: str):
        self.word = word
        self.game_state = set()

    def guess(self, letter: str) -> str:
        self.game_state.add(letter)
        return self.__get_game_state()

    def __get_game_state(self) -> str:
        for letter in self.word:
            if letter not in self.game_state:
                self.game_state.add("_")
        return self.game_state
