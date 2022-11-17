
from enum import Enum

class CommandType(Enum):
    TEA = "T"
    COFFEE = "C"
    CHOCOLATE = "H"


# how do we handle bad sugar inputs?
def drink_maker(command:CommandType, sugar_amt:int) -> str: 
    '''
    '''
    return f"{command.value}:{sugar_amt}:{'0' if sugar_amt>0 else ''}"


def test_drink_maker_coffee_1_sugar():
    assert drink_maker(CommandType.COFFEE, 1) == 'C:1:0'
    
def test_drink_maker_no_sugar():
    assert drink_maker(CommandType.COFFEE, 0) == 'C:0:'

def test_drink_maker_no_sugar():
    assert drink_maker(CommandType.COFFEE, -1) == 'C:0:'