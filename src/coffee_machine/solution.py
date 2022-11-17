
def drink_maker(drink_type:str, sugar_amt:int) -> str: 
    '''
    '''
    return f"{drink_type}:{sugar_amt}:{'0' if sugar_amt>0 else ''}"


def test_drink_maker():

    assert drink_maker('C', 1) == 'C:1:0'
    
    