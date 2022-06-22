import csv


def retrieve_csv(path: str) -> list[list[str]]:
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for line in list(reader):
            lines.append(line)

    return lines
