class HashTable:
    def __init__(self, sz, stp):
        self.storage_size = sz
        self.step = stp
        self.slots = [None] * self.storage_size

    def hash_fun(self, value):
        return sum([ord(ch) for ch in str(value)]) % self.storage_size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        initial_index = index
        while index < self.storage_size:
            if self.slots[index] is None:
                return index
            elif self.slots[index] == value:
                return None
            index += self.step
        index -= self.step
        index = self.step - (self.storage_size - index)
        while index < initial_index:
            if self.slots[index] is None:
                return index
            elif self.slots[index] == value:
                return None
            index += self.step
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        initial_index = index
        while index < self.storage_size:
            if self.slots[index] is not None and self.slots[index] == value:
                return index
            # elif self.slots[index] is None:
            #     return None
            index += self.step
        index -= self.step
        index = self.step - (self.storage_size - index)
        while index < initial_index:
            if self.slots[index] is not None and self.slots[index] == value:
                return index
            # elif self.slots[index] is None:
            #    return None
            index += self.step
        return None


class PowerSet(HashTable):

    def __init__(self):
        self.length = 0
        size = 25000
        step = 3
        super().__init__(size, step)

    def size(self):
        return self.length

    def put(self, value):
        index = super().put(value)
        if index is not None:
            self.length += 1

    def get(self, value):
        return super().find(value) is not None

    def remove(self, value):
        index = super().find(value)
        if index is not None:
            self.length -= 1
            self.slots[index] = None
            return True
        return False

    def intersection(self, set2):
        base = self
        target = set2
        if target.size() < base.size():
            base, target = target, base
        result = PowerSet()
        for value in base.slots:
            if value is not None and target.get(value):
                result.put(value)
        return result

    def union(self, set2):
        base = self
        target = set2
        if target.size() < base.size():
            base, target = target, base
        result = PowerSet()
        result.slots = target.slots
        result.length = target.length
        for value in base.slots:
            if value is not None:
                result.put(value)
        return result

    def difference(self, set2):
        result = PowerSet()
        result.slots = self.slots
        result.length = self.length
        for value in set2.slots:
            if value is not None:
                result.remove(value)
        return result

    def issubset(self, set2):
        for value in set2.slots:
            if value is not None and not self.get(value):
                return False
        return True
