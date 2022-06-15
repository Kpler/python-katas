import csv


def retrieve_csv(path: str):
    lines = []
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        headers = next(reader)
        for r in reader:
            lines.append(r)

    return lines
