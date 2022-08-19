class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum([ord(ch) for ch in value]) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        # print('hash of', value, 'is', index)
        initial_index = index
        while index < self.size and self.slots[index] is not None:
            # print('collision!', value)
            index += self.step
        if index < self.size and self.slots[index] is None:
            return index
        index -= self.step
        index = self.step - (self.size - index)
        while index < initial_index and self.slots[index] is not None:
            index += self.step
        if index < initial_index and self.slots[index] is None:
            return index
        # print('couldnt find slot')
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        initial_index = index
        while index < self.size and self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index += self.step
        if index < self.size and self.slots[index] is None:
            return None
        index -= self.step
        index = self.step - (self.size - index)
        while index < initial_index and self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index += self.step
        return None
