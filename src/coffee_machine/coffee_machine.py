class CoffeeMachine:
    def make_tea(self) -> str:
        return "T::"

    def make_coffee(self):
        return "C::"

    def make_chocolate(self):
        return "H::"

    def add_sugar(self, current_command):
        current_drink, current_sugar_count, current_stick_count = current_command.split(":")
        current_sugar_count = int('0' if current_sugar_count == "" else current_sugar_count)
        if current_sugar_count<2:
            next_sugar_count = current_sugar_count + 1
        return f"{current_drink}:{next_sugar_count}:0"
