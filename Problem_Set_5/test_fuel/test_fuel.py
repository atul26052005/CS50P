import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/5") == 40
    assert convert("99/100") == 99
    assert convert("0/1") == 0

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("2/1")  # X > Y
    with pytest.raises(ValueError):
        convert("hello/world")  # Non-numeric input
    with pytest.raises(ValueError):
        convert("3.5/4")  # Float instead of integer

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Division by zero

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
