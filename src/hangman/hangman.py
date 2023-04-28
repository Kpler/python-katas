class Hangman:

    def __init__(self, word: str):
        self.word = word
        self.game_state = set()
        self.number_of_mistakes = 0
        self.game_ended = False

    def guess(self, letter: str) -> str:
        if self.game_ended:
            return "The game has ended."

        if letter not in self.word:
            self.number_of_mistakes = self.number_of_mistakes + 1
            if self.number_of_mistakes == 6:
                self.game_ended = True
                return "Game over"

        self.game_state.add(letter)
        if self.__is_game_successful():
            self.game_ended = True
            return f"You found the word! ({self.word})"
        return self.__get_game_state()

    def __is_game_successful(self) -> bool:
        for letter in self.word:
            if letter not in self.game_state:
                return False
        return True

    def __get_game_state(self) -> str:
        game_state_str = []
        for letter in self.word:
            if letter not in self.game_state:
                game_state_str.append("_")
            else:
                game_state_str.append(letter)
        return ' '.join(game_state_str)
