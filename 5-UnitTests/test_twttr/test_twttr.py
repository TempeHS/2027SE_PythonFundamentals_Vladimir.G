import twttr


def test_lowercase():
    assert twttr.shorten("hello") == "hll"


def test_uppercase():
    assert twttr.shorten("HELLO") == "HLL"


def test_mixed():
    assert twttr.shorten("Hello") == "Hll"


def test_empty():
    assert twttr.shorten("") == ""


def test_numbers():
    assert twttr.shorten("123") == "123"


def test_vowels():
    assert twttr.shorten("aeiou") == ""


def test_constants():
    assert twttr.shorten("bdc") == "bdc"
