import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Row:
    date: int
    max_temperature: float
    min_temperature: float

    @property
    def spread(self) -> float:
        return self.max_temperature - self.min_temperature


def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for r in list(reader)[:-1]:  # '-1' skip average row
            row = Row(
                date=int(r[0]),
                max_temperature=float(r[1].replace("*", "")),
                min_temperature=float(r[2].replace("*", "")),
            )
            lines.append(row)
        return lines


def find_minimum_spread_date(weather_data: list[Row]) -> float:
    return min(weather_data, key=lambda row: row.spread).date
