class Player:
    def __init__(self, status='love') -> None:
        self.status = status
        #self.score = 0

    def increase_score(self):
        #self.score += 1

        if self.status=='love':
            self.status = '15'
        elif self.status=='15':
            self.status = '30'
        elif self.status=='30':
            self.status = '40'
        elif self.status=='40':
            self.deuce_game()
