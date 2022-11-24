import pytest as pytest

an_example_to_use_parametrize = [42, 42, 42]


@pytest.mark.parametrize("example", an_example_to_use_parametrize)
def test_trivia(example):
    assert 42 == example
