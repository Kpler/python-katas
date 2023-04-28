

class Hangman:
    def __init__(self, result: str) -> None:
        self.result = result
        self.prompt = list("_" * len(self.result))
        self.errors = set()


    def to_str(self):
        return ''.join(self.prompt) + f'{"  # " if self.errors else ""}' + ''.join(self.errors)


    def guess(self, s: str) -> str:

        if s not in self.result:
            self.errors.add(s)

        def c(i: int) -> bool:
            return s == self.result[i]

        indexes = filter(c, range(len(self.result)))
        for idx in indexes:
            self.prompt[idx] = s
        
        if self.prompt == self.result:
            print(f"Success: {self.result}")
        else:
            print(self.prompt)

        return self.to_str()
        