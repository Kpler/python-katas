from src.diamond import make_diamond

def test_print_diamond_with_a():
    expected = "A"
    assert(make_diamond("A")==expected)