import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Row:
    name: str
    goals_scored: int
    goals_taken: int


def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for r in list(reader):
            row = Row(
                name=r[1],
                goals_scored=int(r[6]),
                goals_taken=int(r[7]),
            )
            lines.append(row)
        return lines


def get_min_goal_difference(football_data: list[Row]) -> str:
    return min(football_data, key=lambda row: abs(row.goals_scored - row.goals_taken)).name
