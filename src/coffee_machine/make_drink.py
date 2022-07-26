from logging import exception
from typing import Optional

def make_drink(drink: str, sugar = 0):
  if sugar < 0:
    exception.valueError('Sugar may not be negative')

  drink_code: str
  if drink == "coffee":
    drink_code = 'C'
  elif drink == 'tea':
    drink_code = 'T'
  elif drink == 'chocolate':
    drink_code = 'H'

  if sugar > 0:
    return drink_code + ':' + str(sugar) + ':1'
  return drink_code + '::'
