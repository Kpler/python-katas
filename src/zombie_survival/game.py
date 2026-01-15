class ZombieSurvivalGame:
    def __init__(self) -> None:
        first_survivor = Survivor("henry",game = self)
        self.survivors = [first_survivor]
        self.game_over = False
        pass

class Survivor:
    def __init__(self, name: str, game=None) -> None:
        self.name = name
        self.health = 100
        self.energy = 100
        self.zombie_killed = 0
        self.is_alive = True
        self.game = game

    def decrease(self, property:str, amount:int)->None:
        if property == "health":
            self.health -= amount
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
        elif property == "energy":
            self.energy -= amount
            if self.energy <= 0:
                self.energy = 0

    def increase(self, property:str, amount:int)->None:
        if property == "health":
            self.health += amount
            if self.health >= 100:
                self.health = 100
        elif property == "energy":
            self.energy += amount
            if self.energy >= 100:
                self.energy = 100

    def fight(self) -> None:
        if self.game.game_over:
            return
        if self.energy < 30:
            self.decrease('health',20)
        else:
            self.decrease('health', 10)
            self.zombie_killed += 1
            self.decrease('energy', 30)

    def rest(self) -> None:
        if not self.is_alive:
            return
        self.increase('energy',40)

    def heal(self)->None:
        if self.energy >= 20:
            self.decrease("energy", 20)
            self.increase("health", 25)

    def run_away(self)->None:
        self.game.game_over = True