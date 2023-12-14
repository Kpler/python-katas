class CoffeeMachine:

    def order(self, drink_type, sugar):
        drink_dict ={
            "Tea": "T",
            "Coffee": "C",
            "Chocolate": "H",
        }
        _drink = drink_dict.get(drink_type)
        _sugar = sugar if sugar else ""
        _stick = "0" if sugar else ""
        command = f"{_drink}:{_sugar}:{_stick}"
        return command

    def print_message(self, message):
        return f"M:{message}"
