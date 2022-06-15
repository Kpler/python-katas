import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Row:
    date: int
    max_temperature: float
    min_temperature: float

    @property
    def spread(self):
        return self.max_temperature - self.min_temperature


def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)

        lines = []
        for r in list(reader)[:-1]:
            row = Row(date=int(r[0]),
                      max_temperature=float(r[1].replace("*", "")),
                      min_temperature=float(r[2].replace("*", ""))
                      )
            lines.append(row)
        return lines


def find_minimum_spread_date(weather_data: list) -> int:
    date_and_spread = [
        (r.date, r.spread)
        for r in weather_data
    ]
    return min(date_and_spread, key=lambda x: x[1])[0]
