from dataclasses import dataclass


@dataclass(frozen=True)
class MolkkyScore:
    value: int


@dataclass(frozen=True, kw_only=True)
class MolkkyGame:
    score: MolkkyScore = MolkkyScore(0)

    def pin_down(self, pin_numbers: list[int]) -> "MolkkyGame":
        if len(pin_numbers) == 1:
            score = pin_numbers[0]
        else:
            score = len(pin_numbers)

        return MolkkyGame(score=MolkkyScore(self.score.value + score))
