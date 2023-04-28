from enum import Enum


class GameStatus(Enum):
    PLAYING = 1
    WON = 2
    LOST = 3


class Hangman:
    MISTAKES_ALLOWED = 6
    HIDE_CHARACTER = '_'

    def __init__(self, word: str):
        self._word = word
        self._mistakes_left = self.MISTAKES_ALLOWED
        self._current_word = self.HIDE_CHARACTER*len(self._word)
        self._failed_letters = ""
        self.game_status = GameStatus.PLAYING

    def _format_result(self) -> str:
        part1 = " ".join(self._current_word)
        part2 = " # " if self._failed_letters else ""
        part3 = self._failed_letters

        return part1 + part2 + part3

    def guess(self, letter: str) -> str:
        if self.game_status != GameStatus.PLAYING:
            return "The game has ended."
        result = self._format_result()
        if letter in result:
            return result
        if letter in self._word:
            for pos, char in enumerate(self._word):
                if char == letter:
                    self._current_word = self._current_word[:pos] + letter + self._current_word[pos+1:]
            if self._current_word == self._word:
                self.game_status = GameStatus.WON
                return f"You found the word! ({self._word})"
        else:
            self._mistakes_left -= 1
            if self._mistakes_left <= 0:
                self.game_status = GameStatus.LOST
                return f"You got hung! The word was {self._word}."
            self._failed_letters += letter

        return self._format_result()
