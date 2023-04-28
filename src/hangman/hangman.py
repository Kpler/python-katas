

class Hangman:

    MAX_MISTAKES_ALLOWED = 6

    def __init__(self, result: str) -> None:
        self.result = result
        self.prompt = list("_" * len(self.result))
        self.errors = set()


    def _to_str(self):
        return ''.join(self.prompt) + f'{" # " if self.errors else ""}' + ''.join(self.errors)

    def _is_finished_in_success(self):
        return self.prompt == list(self.result)

    def _is_finished_in_failed(self):
        return len(self.errors) > self.MAX_MISTAKES_ALLOWED

    def _is_finished(self):
        return self._is_finished_in_success() or self._is_finished_in_failed()

    def guess(self, s: str) -> str:
        if self._is_finished():
            return "# The game has ended"

        if s not in self.result:
            self.errors.add(s)
            if self._is_finished_in_failed():
                return f"# You got hung! The word was {self.result}."

        def c(i: int) -> bool:
            return s == self.result[i]

        indexes = filter(c, range(len(self.result)))
        for idx in indexes:
            self.prompt[idx] = s
        
        if self._is_finished_in_success():
            return f"# You found the word! ({self.result})"

        return self._to_str()
        