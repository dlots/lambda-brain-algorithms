import unittest
from random import shuffle
from array_binary_search_tree import aBST, calculate_tree_size


class TestArrayBinarySearchTree(unittest.TestCase):
    def test_calculate_tree_size(self):
        self.assertEqual(calculate_tree_size(0), 1)
        self.assertEqual(calculate_tree_size(1), 3)
        self.assertEqual(calculate_tree_size(2), 7)
        self.assertEqual(calculate_tree_size(3), 15)
        self.assertEqual(calculate_tree_size(4), 31)

    def test_find_in_empty_tree(self):
        tree = aBST(5)
        for key in range(100):
            index = tree.FindKeyIndex(key)
            self.assertEqual(index, 0)
            self.assertIsNone(tree.Tree[index])

    def test_make_full_tree(self):
        depth = 2
        tree = aBST(depth)
        keys = [10, 5, 15, 2, 6, 12, 17]
        for key in keys:
            index = tree.AddKey(key)
            self.assertGreaterEqual(index, 0)
            self.assertEqual(tree.Tree[index], key)
            self.assertEqual(tree.FindKeyIndex(key), index)
        for key in keys:
            self.assertGreaterEqual(tree.FindKeyIndex(key), 0)

    def test_cant_exceed_depth_tree_is_not_full(self):
        depth = 2
        tree = aBST(depth)
        keys = [10, 5, 2, 6]
        for key in keys:
            tree.AddKey(key)
        self.assertEqual(tree.AddKey(1), -1)
        self.assertEqual(tree.AddKey(7), -1)


if __name__ == '__main__':
    unittest.main()
