import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.resize_down_threshold = 0.5
        self.resize_down_rate = 1.5
        self.minimal_capacity = 16

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    # complexity - O(n)
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count:
            self.append(itm)
            return
        if self.count + 1 > self.capacity:
            self.resize(2 * self.capacity)
        for x in reversed(range(i, self.count)):
            self.array[x + 1] = self.array[x]
        self.array[i] = itm
        self.count += 1

    # complexity - O(n)
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        new_count = self.count - 1
        new_capacity = max(int(self.capacity / self.resize_down_rate), self.minimal_capacity)
        if new_capacity != self.capacity and new_count / self.capacity < self.resize_down_threshold:
            self.resize(new_capacity)
        self.count -= 1
        for x in range(i, self.count):
            self.array[x] = self.array[x + 1]
