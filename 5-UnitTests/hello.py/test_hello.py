from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_arugument():
    for name in ["Hermonine", "Harry", "Ron"]:
        assert hello(name) == "hello, {name}"
