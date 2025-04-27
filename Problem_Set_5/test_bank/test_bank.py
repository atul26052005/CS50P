from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, how are you?") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hola") == 20  # Spanish for Hello but starts with 'H'
    assert value("howdy") == 20
    assert value("Hmmm") == 20

def test_other_words():
    assert value("Good morning") == 100
    assert value("What's up?") == 100
    assert value("Bye") == 100
    assert value("123hello") == 100  # Doesn't start with "hello"
    assert value("greetings") == 100

