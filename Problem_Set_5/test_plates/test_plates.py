import pytest
from plates import is_valid

def main():
    test_length()
    test_first_two()
    test_space_punctuation()
    test_num_not_in_middle()

def test_length():
    assert is_valid("HELLO") == True
    assert is_valid("C") == False

def test_first_two():
    assert is_valid("CS") == True
    assert is_valid("50") == False

def test_space_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS, 50") == False

def test_num_not_in_middle():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

if __name__ == "__main__":
    main()
