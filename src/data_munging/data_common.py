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


def retrieve_csv(path: str, index_label: int, index_min: int, index_max: int):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers
        
        lines = []
        for r in list(reader):  # '-1' skip average row
            lines.append(parse_row(r, index_label, index_min, index_max))
        return lines


def parse_row(raw: list, index_label: int, index_min: int, index_max: int):
    return Row(
        label=raw[index_label],
        min_value=float(raw[index_min]),
        max_value=float(raw[index_max])
    )


def get_min_spread(data: list[Row]):
    return min(data, key=lambda row: abs(row.delta)).label
