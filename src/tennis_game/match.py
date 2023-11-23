class Match():
    def __init__(self) -> None:
        self.player1_score = "L"
        self.player2_score = "L"

        self.player1_points = 0
        self.player1_points = 0

        self.point_dict = {
            0: "L",
            1: "15",
            2: "30",
            3: "40",
        }

    def add_point_to_player1(self):
        self.player1_points += 1 
        self.player1_score = self.point_dict.get(self.player1_points)
    
    def add_point_to_player2(self):
        self.player2_points += 1 
        self.player2_score = self.point_dict.get(self.player2_points)

    def game(self):
        pass
