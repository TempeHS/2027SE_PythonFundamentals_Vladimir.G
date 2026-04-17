import fuel
import pytest


def test_percent():
    assert fuel.calculate("4/4") == 100
    assert fuel.calculate("3/4") == 75
    assert fuel.calculate("2/4") == 50
    assert fuel.calculate("1/4") == 25
    assert fuel.calculate("0/4") == 0


def test_x_greater_y():
    with pytest.raises(ValueError):
        fuel.calculate("5/4")


def test_non_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        fuel.calculate("1/0")


def test_invalid_string():
    with pytest.raises(ValueError):
        fuel.calculate("Cat/Dog")
