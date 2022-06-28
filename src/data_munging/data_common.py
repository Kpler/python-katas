import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Row:
    label: str
    max_value: float
    min_value: float

    @property
    def delta(self) -> float:
        return self.max_value - self.min_value

def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for r in list(reader):  # '-1' skip average row
            row = Row(
                label=str(r[0]),
                max_value=float(r[1].replace("*", "")),
                min_value=float(r[2].replace("*", "")),
            )
            lines.append(row)
        return lines