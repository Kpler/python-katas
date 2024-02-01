from dataclasses import dataclass
from enum import Enum


class Pin(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12


@dataclass(frozen=True)
class MolkkyScore:
    value: int


@dataclass(frozen=True)
class PinScore:
    value: list[Pin]

    def get_score(self) -> MolkkyScore:
        if len(self.value) == 1:
            score = self.value[0].value
        else:
            score = len(self.value)

        return MolkkyScore(score)


@dataclass(frozen=True, kw_only=True)
class MolkkyGame:
    score: MolkkyScore = MolkkyScore(0)

    def pin_down(self, pin_numbers: list[Pin]) -> "MolkkyGame":
        score = PinScore(pin_numbers).get_score()

        return MolkkyGame(score=MolkkyScore(self.score.value + score.value))
