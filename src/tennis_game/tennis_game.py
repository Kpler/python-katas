class Player:
    def __init__(self) -> None:
        self.score = 0
        self.score_to_status = {
            0: "love",
            1: "15",
            2: "30",
            3: "40",
            4: "deuce",
        }

    def increase_score(self):
        self.score += 1

    def get_status(self):
        return self.score_to_status[self.score]
