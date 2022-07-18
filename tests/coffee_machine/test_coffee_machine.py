from src.coffee_machine.coffee_machine import make_drink


def test_make_tea_with_one_sugar():
    result = make_drink("tea", "1", "1")
    assert result == "T:1:1"


def test_make_chocolate_without_sugar():
    result = make_drink("chocolate", "0", "0")
    assert result == "H:0:0"


def test_make_coffee_without_sugar():
    result = make_drink("coffee", "2", "1")
    assert result == "C:2:1"
