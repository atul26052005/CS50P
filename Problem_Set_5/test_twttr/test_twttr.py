from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("HelloWorld") == "HllWrld"
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"  # Numbers should remain unchanged

def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_empty_string():
    assert shorten("") == ""

