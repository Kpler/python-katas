from dataclasses import dataclass
from enum import Enum


MAX_SCORE = 50
CHECKPOINT_SCORE = 25

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

    def append(self, score: "MolkkyScore") -> "MolkkyScore":
        new_value = self.value + score.value
        if new_value > MAX_SCORE:
            new_value = CHECKPOINT_SCORE
        return MolkkyScore(new_value)


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

        return MolkkyGame(score=self.score.append(score))
