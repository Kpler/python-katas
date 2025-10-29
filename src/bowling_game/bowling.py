

class Game:
    def __init__(self):
        self.rolls: list[int] = [0] * 21
        self.current_roll: int = 0
        self.score: int = 0
        self.is_last_frame_a_strike: bool = False

    def roll(self, pins: int):
        print(self.get_game_state())
        self.rolls[self.current_roll] = pins
        self.current_roll += 1
        self.update_score(pins)
        if (pins == 10 and self.current_roll%2 == 1):
            self.is_last_frame_a_strike = True
            self.current_roll += 1
        elif self.current_roll%2 == 0:
            self.is_last_frame_a_strike = False


    def update_score(self, pins: int):
        self.score += pins
        if self.is_last_frame_a_strike:
            self.score += pins
    
    def get_game_state(self):
        return (self.current_roll, self.score, self.is_last_frame_a_strike)