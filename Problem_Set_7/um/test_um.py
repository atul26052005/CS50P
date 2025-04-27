import pytest
from um import count

def test_single_um():
    assert count("Um, I don't know.") == 1
    assert count("um.") == 1
    assert count("hello, um, world") == 1

def test_multiple_um():
    assert count("um um um") == 3
    assert count("Um... um! UM?") == 3
    assert count("um, um, um, um.") == 4

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("sum of numbers") == 0
    assert count("Umbridge is a character in Harry Potter") == 0

def test_um_with_other_words():
    assert count("Um, do you understand?") == 1
    assert count("That's, um, interesting.") == 1
    assert count("Umm... I'm not sure.") == 0  # 'Umm' should not be counted

def test_case_insensitivity():
    assert count("UM, um, Um, uM") == 4
