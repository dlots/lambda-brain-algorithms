class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def __generate_tree_recursively(self, array, begin, end, current_level, parent):
        array_length = end - begin
        if array_length < 0:
            raise IndexError('somethings wrong with array bounds')
        if array_length == 0:
            return None
        middle = begin + int(array_length / 2)
        sub_root = BSTNode(array[middle], parent)
        sub_root.Level = current_level
        if array_length > 1:
            sub_root.LeftChild = self.__generate_tree_recursively(array, begin, middle, current_level + 1, sub_root)
            sub_root.RightChild = self.__generate_tree_recursively(array, middle + 1, end, current_level + 1, sub_root)
        return sub_root

    def GenerateTree(self, a):
        a.sort()
        self.Root = self.__generate_tree_recursively(a, 0, len(a), 0, None)

    def __is_balanced_recursive(self, sub_root):
        if sub_root is None:
            return True, 0
        left_balanced, left_depth = self.__is_balanced_recursive(sub_root.LeftChild)
        if not left_balanced:
            return False, None
        right_balanced, right_depth = self.__is_balanced_recursive(sub_root.RightChild)
        tree_is_balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
        return tree_is_balanced, max(left_depth, right_depth) + 1

    def IsBalanced(self, root_node):
        tree_is_balanced, _ = self.__is_balanced_recursive(root_node)
        return tree_is_balanced
