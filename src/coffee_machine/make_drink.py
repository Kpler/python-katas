from typing import Optional

def make_drink(drink: str, sugar = 0):
  if drink == "coffee":
    drink_code = 'C'
    if sugar > 0:
      return 'C:' + str(sugar) + ':1'
    return 'C::'