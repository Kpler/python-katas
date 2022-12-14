from diamond.diamond import make_diamond


def test_print_diamond_with_a():
    expected = "A"
    assert(make_diamond("A")==expected)


def test_print_diamond_with_ab():
    expected = " A \nB B\n A "
    assert make_diamond("B") == expected