class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity;
        self.size = 0;

    def __str__(self):
        return f"🍪" * self._size;

    def deposit(self, n):
        self.size += n;

    def withdraw(self, n):
        self.size -= n;

    @property
    def capacity(self):
        return self._capacity;

    @capacity.setter
    def capacity(self, capacity):
        try:
            self._capacity = int(capacity);

        except ValueError:
            raise ValueError;

        if capacity <= 0:
            raise ValueError;

        self._capacity = capacity;

    @property
    def size(self):
        return self._size;

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError;

        if size > self.capacity:
            raise ValueError;

        self._size = size;

