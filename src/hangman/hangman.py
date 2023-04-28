

class Hangman:
    def __init__(self, result: str) -> None:
        self.result = result
        self.prompt = "_" * len(self.result)
        
    def guess(self, s: str) -> None:
        def c(i: int) -> bool:
            return s in self.result
        l = list(range(len(self.result)))
        indexes = filter(c, l)
        for idx in indexes:
            self.prompt[idx] = s
        
        if self.prompt == self.result:
            print(f"Success: {self.result}")
        else:
            print(self.prompt)
        