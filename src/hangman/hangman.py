

class Hangman:
    def __init__(self, result: str) -> None:
        self.result = result
        self.prompt = list("_" * len(self.result))
        self.errors = set()
        
    def guess(self, s: str) -> str:

        if s not in self.result:
            self.errors.add(s)

        def c(i: int) -> bool:
            return s == self.result[i]
        l = list(range(len(self.result)))
        indexes = filter(c, l)
        for idx in indexes:
            self.prompt[idx] = s
        
        if self.prompt == self.result:
            print(f"Success: {self.result}")
        else:
            print(self.prompt)

        return ''.join(self.prompt) + ' # ' + ''.join(self.errors)
        