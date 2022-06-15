import csv


def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)

        return list(reader)


def find_minimum_spread_date(weather_data: list) -> int:
    weather_data = weather_data[:-1]
    date_and_spread = [
        (int(r[0]), float(r[1].replace("*", "")) - float(r[2].replace("*", "")))
        for r in weather_data
    ]
    return min(date_and_spread, key=lambda x: x[1])[0]
