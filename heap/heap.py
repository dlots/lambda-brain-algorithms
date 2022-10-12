def get_tree_capacity_from_depth(depth):
    capacity = 0
    for x in range(depth + 1):
        capacity += 2 ** x
    return capacity


def get_parent_index(current_index):
    return int((current_index - 1) / 2)


def get_left_child_index(current_index):
    return 2 * current_index + 1


def get_right_child_index(current_index):
    return 2 * current_index + 2


class Heap:
    def __init__(self):
        self.HeapArray = []
        self.size = 0

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * get_tree_capacity_from_depth(depth)
        self.size = 0
        for key in a:
            self.Add(key)

    def __get_max_child_index(self, index):
        max_index = None
        left_child_index = get_left_child_index(index)
        if left_child_index < self.size:
            max_index = left_child_index
        right_child_index = get_right_child_index(index)
        if right_child_index < self.size and (max_index is None or self.HeapArray[max_index] < self.HeapArray[right_child_index]):
            max_index = right_child_index
        return max_index

    def GetMax(self):
        if self.size == 0:
            return -1
        max_element = self.HeapArray[0]
        self.size -= 1
        self.HeapArray[0] = self.HeapArray[self.size]
        self.HeapArray[self.size] = None
        sift_index = 0
        max_child_index = self.__get_max_child_index(sift_index)
        while max_child_index is not None and self.HeapArray[sift_index] < self.HeapArray[max_child_index]:
            self.HeapArray[sift_index], self.HeapArray[max_child_index] = self.HeapArray[max_child_index], self.HeapArray[sift_index]
            sift_index = max_child_index
            max_child_index = self.__get_max_child_index(sift_index)
        return max_element

    def Add(self, key):
        if self.size == len(self.HeapArray):
            return False
        new_key_index = self.size
        self.HeapArray[new_key_index] = key
        parent_index = get_parent_index(new_key_index)
        while new_key_index != 0 and self.HeapArray[new_key_index] > self.HeapArray[parent_index]:
            self.HeapArray[new_key_index], self.HeapArray[parent_index] = self.HeapArray[parent_index], self.HeapArray[new_key_index]
            new_key_index = parent_index
            parent_index = get_parent_index(new_key_index)
        self.size += 1

