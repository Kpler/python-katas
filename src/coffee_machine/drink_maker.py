class DrinkMaker:
    def make(
        self,
        drink: str,
    ):
        if drink == "Tea":
            command = "T::"
        elif drink == "Hot Chocolate":
            command = "H::"
        else:
            raise (Exception)
        return command
