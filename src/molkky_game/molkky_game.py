from dataclasses import dataclass


@dataclass(frozen=True)
class MolkkyScore:
    value: int


@dataclass(frozen=True, kw_only=True)
class MolkkyGame:
    score: MolkkyScore = MolkkyScore(0)

    def pin_down(self, pin_number: int) -> "MolkkyGame":
        return MolkkyGame(score=MolkkyScore(self.score.value + pin_number))
