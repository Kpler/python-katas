class Game:
    def __init__(self) -> None:
        self.rolls: list[int] = []

    def roll(self, count: int) -> None:
        self.rolls.append(count)

        if count == 10 and len(self.rolls) % 2 == 1:
            self.rolls.append(0)

    def is_spare(self, index: int) -> bool:
        is_even = index%2 == 0
        penultimate_roll = self.rolls[index-2] if index >= 2 else 0
        previous_roll = self.rolls[index-1] if index >= 2 else 0
        return penultimate_roll + previous_roll == 10 and penultimate_roll != 10 and is_even

    def is_strike(self, index: int) -> bool:
        is_odd = index%2 == 1
        antipenultimate_roll = self.rolls[index-3] if index >= 3 else 0
        penultimate_roll = self.rolls[index-2] if index >= 2 else 0
        return (antipenultimate_roll == 10 and is_odd) or (penultimate_roll == 10 and not is_odd)

    def score(self) -> int:
        output = 0
        for index, roll in enumerate(self.rolls):
            output += roll
            if self.is_spare(index):
                output += roll
            if self.is_strike(index):
                output += roll
        return output
