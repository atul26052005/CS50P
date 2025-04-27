import pytest
from working import convert

def test_valid_inputs():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:30 AM to 4:45 PM") == "01:30 to 16:45"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # Missing spaces
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Invalid minutes
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")  # Wrong separator

def test_edge_cases():
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("11 PM to 12 AM") == "23:00 to 00:00"
