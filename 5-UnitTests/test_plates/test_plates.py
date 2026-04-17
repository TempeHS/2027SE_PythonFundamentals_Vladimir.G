import plates


def test_length():
    assert plates.is_valid_length("A") is False
    assert plates.is_valid_length("AAAA") is True
    assert plates.is_valid_length("AAAAAAA") is False


def test_prefix():
    assert plates.is_valid_prefix("AA") is True
    assert plates.is_valid_prefix("A1") is False


def test_tail():
    assert plates.is_valid_tail("AAAA02") is False
    assert plates.is_valid_tail("AAAA20") is True
    assert plates.is_valid_tail("AAAA2A") is False


def test_characters():
    assert plates.is_valid("AA.AA") is False
    assert plates.is_valid("AA AA") is False
    assert plates.is_valid("AA?AA") is False
    assert plates.is_valid("AAAA22") is True
