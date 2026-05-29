from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/100") == 1
    assert convert("50/100") == 50
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_value_error():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-2/3")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
