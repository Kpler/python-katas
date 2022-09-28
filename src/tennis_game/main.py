class Game(object):

    score_list = ["love", "15", "30", "40"]

    def __init__(self):
        self.game_score = [0, 0]

    def score(self):
        return f"{self.score_list[self.game_score[0]]}-{self.score_list[self.game_score[1]]}"

    def score_point(self, player_number):
        self.game_score[player_number] += 1
        if self.game_score[player_number] > len(self.score_list) - 1:
            raise Exception(f"Player {player_number + 1} wins !")
