class CoffeeMachine:
    def order(self, drink_type, sugar, money, hot=False):
        drink_dict = {
            "Tea": ["T", 0.4],
            "Coffee": ["C", 0.6],
            "Chocolate": ["H", 0.5],
            "Orange Juice": ["O", 0.6]
        }
        drink_money = drink_dict.get(drink_type)[1]
        if money < drink_money:
            return self.print_message(f"missing {round(drink_money - money, 2)}")
        _drink = drink_dict.get(drink_type)[0]
        _hot = "h" if hot else ""
        _sugar = sugar if sugar else ""
        _stick = "0" if sugar else ""
        command = f"{_drink}{_hot}:{_sugar}:{_stick}"
        return command

    def print_message(self, message):
        return f"M:{message}"
