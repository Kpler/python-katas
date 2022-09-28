class Game(object):

    SCORE_LIST = ["love", "15", "30", "40", "adv"]
    MAX_SCORE = len(SCORE_LIST) - 2

    def __init__(self):
        self.game_score = [0, 0]

    def score(self):
        if self.game_score == [self.MAX_SCORE, self.MAX_SCORE]:
            return f"deuce"

        return f"{self.SCORE_LIST[self.game_score[0]]}-{self.SCORE_LIST[self.game_score[1]]}"

    def score_point(self, player_number):
        self.game_score[player_number] += 1

        if self.game_score[player_number] == self.MAX_SCORE + 1 and self.game_score[1 - player_number] < self.MAX_SCORE:
            self.game_score[player_number] += 1

        if self.game_score[player_number] == self.MAX_SCORE + 1 and self.game_score[1 - player_number] == self.MAX_SCORE + 1:
            self.game_score[player_number] -= 1
            self.game_score[1 - player_number] -= 1

        if self.game_score[player_number] > self.MAX_SCORE + 1:
            raise Exception(f"Player {player_number + 1} wins !")
