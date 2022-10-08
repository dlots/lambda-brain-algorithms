def calculate_tree_size(depth):
    size = 0
    for x in range(depth + 1):
        size += 2 ** x
    return size


def get_parent_index(current_index):
    return (current_index - 1) / 2


def get_left_child_index(current_index):
    return 2 * current_index + 1


def get_right_child_index(current_index):
    return 2 * current_index + 2


class aBST:

    def __init__(self, depth):
        tree_size = calculate_tree_size(depth)
        self.Tree = [None] * tree_size

    def find_key_index_recursively(self, key, current_index):
        if current_index >= len(self.Tree):
            return None
        current_key = self.Tree[current_index]
        if current_key is None:
            return -current_index
        if key == current_key:
            return current_index
        next_index = None
        if key < current_key:
            next_index = get_left_child_index(current_index)
        if key > current_key:
            next_index = get_right_child_index(current_index)
        return self.find_key_index_recursively(key, next_index)

    def FindKeyIndex(self, key):
        return self.find_key_index_recursively(key, 0)

    def AddKey(self, key):
        key_index = self.FindKeyIndex(key)
        if key_index is None:
            return None
        if key_index < 0 or (key_index == 0 and self.Tree[0] is None):
            key_index = -key_index
            self.Tree[key_index] = key
            return key_index
        return key_index
