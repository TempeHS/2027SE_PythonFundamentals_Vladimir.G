class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity or n < 0:
            raise ValueError("Cookies exceed capacity")

        self._size += n

    def withdraw(self, n):
        if self._size - n < 0 or n < 0:
            raise ValueError("Not enough cookie")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
