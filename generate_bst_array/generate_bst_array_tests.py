import unittest
from random import sample
from generate_bst_array import GenerateBBSTArray, get_left_child_index, get_right_child_index
from array_binary_search_tree.array_binary_search_tree import get_tree_size_from_depth


class MyTestCase(unittest.TestCase):
    def test_generate_balanced_bst_array(self):
        array = [43, 12, 22, 0, 46, 21, 100]
        balanced_tree_array = GenerateBBSTArray(array)
        for index, key in enumerate(balanced_tree_array):
            self.assertIsNotNone(key)
            left_child_index = get_left_child_index(index)
            if left_child_index < len(balanced_tree_array):
                self.assertLess(balanced_tree_array[left_child_index], key)
            right_child_index = get_right_child_index(index)
            if right_child_index < len(balanced_tree_array):
                self.assertGreater(balanced_tree_array[right_child_index], key)

    def test_generate_balanced_bst_array_randomized(self):
        for depth in range(10):
            size = get_tree_size_from_depth(depth)
            array = sample(range(10000), size)
            balanced_tree_array = GenerateBBSTArray(array)
            for index, key in enumerate(balanced_tree_array):
                self.assertIsNotNone(key)
                left_child_index = get_left_child_index(index)
                if left_child_index < len(balanced_tree_array):
                    self.assertLess(balanced_tree_array[left_child_index], key)
                right_child_index = get_right_child_index(index)
                if right_child_index < len(balanced_tree_array):
                    self.assertGreater(balanced_tree_array[right_child_index], key)


if __name__ == '__main__':
    unittest.main()
