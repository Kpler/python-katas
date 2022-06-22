import csv

def compute_difference(row: list[str]) -> int:
    goals_scored = int(row[6])
    goals_taken = int(row[7])
    return goals_scored - goals_taken

def retrieve_csv(path: str) -> list[list[str]]:
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for line in list(reader):
            lines.append(line)

    return lines
