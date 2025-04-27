from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate("10.20.30.40") == True
    assert validate("10.20.30") == False
    assert validate("10.20") == False
    assert validate("10") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"256.1.1.1") == False
    assert validate(r"1.256.1.1") == False
    assert validate(r"1.2.256.1") == False
    assert validate(r"1.1.1.256") == False

if __name__ == "__main__":
    main()
