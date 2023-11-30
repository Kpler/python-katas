class Player:
    def __init__(self, name: str):
        self.points = 0
        self.name = name

class Game:

    def __init__(self):
        self.player1 = Player("player1")
        self.player2 = Player("player2")

        self.score_table = {
            0: "love",
            1: "15",
            2: "30",
            3: "40",
        }

    def get_score(self, player):
        return self.score_table.get(player.points)

    def get_winner(self):
        if self.player1.points > 3 and (self.player1.points - self.player2.points) > 1:
            return self.player1.name
        elif self.player2.points > 3 and (self.player2.points - self.player1.points) > 1:
            return self.player2.name
        else:
            return None

    def add_points(self, player):
        player.points += 1

    def print_score(self):
        winner = self.get_winner()
        if winner is not None:
            return f"{winner} winner"
        elif self.player1.points < 4 and self.player2.points < 4:
            return f"{self.score_table.get(self.player1.points)}:{self.score_table.get(self.player2.points)}"
        elif self.player1.points > self.player2.points:
            return f"player1 adv"
        elif self.player1.points < self.player2.points:
            return f"player2 adv"
        else:
            return "deuce"