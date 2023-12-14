class CoffeeMachine:
    def order(self, drink_type, sugar, money):
        drink_dict = {
            "Tea": ["T", 0.4],
            "Coffee": ["C", 0.6],
            "Chocolate": ["H", 0.5],
        }
        if money < drink_dict.get(drink_type)[1]:
            return None
        _drink = drink_dict.get(drink_type)[0]
        _sugar = sugar if sugar else ""
        _stick = "0" if sugar else ""
        command = f"{_drink}:{_sugar}:{_stick}"
        return command

    def print_message(self, message):
        return f"M:{message}"
