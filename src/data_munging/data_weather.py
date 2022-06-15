import csv


def retrieve_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)

        return list(reader)


def find_minimum_spread_date(weather_data: list):
    return 2