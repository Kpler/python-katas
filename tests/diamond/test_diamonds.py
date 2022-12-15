from src.diamond.diamonds import build_diamond
import pytest


def test_build_diamond_return_given_A():
    assert build_diamond('A') == 'A'


def test_build_diamond_return_given_B():
    assert build_diamond('B') == " A \n B B\n  A "