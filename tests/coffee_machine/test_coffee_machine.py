from src.coffee_machine.coffee_machine import make_drink


def test_make_tea_with_one_sugar():
    result = make_drink("tea", 1)
    assert result == "T:1:0"


def test_make_chocolate_without_sugar():
    result = make_drink("chocolate", 0)
    assert result == "H::"


def test_make_tea_without_sugar():
    result = make_drink("tea")
    assert result == "T::"
