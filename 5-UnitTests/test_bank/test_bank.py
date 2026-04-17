import bank


def test_hello():
    # Error created from removed casefold()
    assert bank.greeting_value("Hello") == 0

    assert bank.greeting_value("hello") == 0

    # Error created from removed casefold()
    assert bank.greeting_value("HELLO") == 0


def test_h():
    assert bank.greeting_value("h") == 20
    assert bank.greeting_value("hi") == 20
    assert bank.greeting_value("hey") == 20


def test_others():
    assert bank.greeting_value("Good Day") == 100
    assert bank.greeting_value("Whats up") == 100
    assert bank.greeting_value(" ") == 100
