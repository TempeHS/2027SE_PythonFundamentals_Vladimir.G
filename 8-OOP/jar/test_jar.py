from jar import Jar

import pytest
import random


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    capacity = random.randint(0, 1000)
    jar = Jar(capacity=capacity)
    assert jar.capacity == capacity
    assert jar.size == 0


def test_init_raises():
    with pytest.raises(ValueError):
        Jar(capacity=-1)
    with pytest.raises(ValueError):
        Jar(capacity=random.randint(-1000, -1))


# test str
def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(10)
    assert str(jar) == "🍪" * 10


def test_deposit():
    jar = Jar(capacity=12)

    jar.deposit(10)
    assert jar.size == 10
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        jar.deposit(20)

    with pytest.raises(ValueError):
        jar.deposit(-20)


def test_withdraw():
    jar = Jar(capacity=12)

    with pytest.raises(ValueError):
        jar.withdraw(5)

    jar.withdraw(0)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(-10)

    jar.deposit(10)
    jar.withdraw(5)

    assert jar.size == 5
    assert jar.capacity == 12
