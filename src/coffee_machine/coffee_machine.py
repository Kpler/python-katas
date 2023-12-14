class CoffeeMachine:

    def order(self, drink_type, sugar, ):
        _drink = "T" if drink_type == "Tea" else ""
        _sugar = sugar if sugar else ""
        _stick = "0" if sugar else ""
        command = f"{_drink}:{_sugar}:{_stick}"
        return command
