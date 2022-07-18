

def make_drink(input: str, number_of_sugar: str, number_of_stick: str) -> str:
    first_char: str
    
    if input=="tea":
      first_char="T"
    elif input=="chocolate":
      first_char="H"
    elif input=="coffee":
      first_char="C"

    second_char: str

    if number_of_sugar == "1":
      second_char= "1"
    elif number_of_sugar == "0":
      second_char = "0"
    elif number_of_sugar == "2":
      second_char = "2"

    third_char: str

    if number_of_stick == "1":
      third_char= "1"
    elif number_of_stick == "0":
      third_char = "0"
    return first_char + ":" + second_char + ":" + third_char
