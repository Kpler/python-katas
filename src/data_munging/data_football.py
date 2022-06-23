import csv

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