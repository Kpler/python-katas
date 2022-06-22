import csv


@dataclass(frozen=True)
class FootballTeam:
    team: str
    goals_scored: int
    goals_taken: int

    def __init__(row: list[str]):
        pass

    @property
    def compute_difference(self) -> int:
        return abs(self.goals_scored - self.goals_taken)


def compute_difference(row: list[str]) -> (str, int):
    goals_scored = int(row[6])
    goals_taken = int(row[7])
    team = row[1]
    return team, abs(goals_scored - goals_taken)


def retrieve_csv(path: str) -> list[list[str]]:
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        _ = next(reader)  # skip csv headers

        lines = []
        for line in list(reader):
            lines.append(line)

    return lines

def compute_smallest_difference(data: list[list[str]]) -> str:
    team_differences = [compute_difference(row) for row in data]
    return min(team_differences, key=lambda team: team[1])[0]


def compute_football_loser(path: str) -> str:
    content = retrieve_csv(path)
    return compute_smallest_difference(content)
