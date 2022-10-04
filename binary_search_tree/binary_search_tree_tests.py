import unittest
from random import shuffle
from binary_search_tree import BST, BSTNode


def value_from_key(key):
    return key ** 2


def count_nodes_recursively(subtree_root):
    if subtree_root is None:
        return 0
    return count_nodes_recursively(subtree_root.LeftChild) + count_nodes_recursively(subtree_root.RightChild) + 1


def count_nodes_in_tree(tree):
    return count_nodes_recursively(tree.Root)


class TestBinarySearchTree(unittest.TestCase):
    def test_find_node_by_key(self):
        tree = BST(None)
        result = tree.FindNodeByKey(100)
        self.assertIsNone(result.Node)
        keys = [10, 4, 15]
        for key in keys:
            tree.AddKeyValue(key, value_from_key(key))
        for key in keys:
            result = tree.FindNodeByKey(key)
            self.assertIsNotNone(result.Node)
            self.assertEqual(result.Node.NodeKey, key)
            self.assertTrue(result.NodeHasKey)
        result = tree.FindNodeByKey(3)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertTrue(result.ToLeft)
        result = tree.FindNodeByKey(5)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertFalse(result.ToLeft)

    def test_add_key_value(self):
        tree = BST(None)
        keys = [10, 4, 15]
        for i, key in enumerate(keys):
            result = tree.FindNodeByKey(key)
            self.assertTrue(result.Node is None or not result.NodeHasKey)
            self.assertTrue(tree.AddKeyValue(key, value_from_key(key)))
            result = tree.FindNodeByKey(key)
            self.assertIsNotNone(result.Node)
            self.assertEqual(result.Node.NodeKey, key)
            self.assertTrue(result.NodeHasKey)
            self.assertEqual(result.Node.NodeValue, value_from_key(key))
            if key == 4:
                self.assertIs(result.Node, tree.Root.LeftChild)
                self.assertIs(result.Node.Parent, tree.Root)
            elif key == 15:
                self.assertIs(result.Node, tree.Root.RightChild)
                self.assertIs(result.Node.Parent, tree.Root)
            else:
                self.assertIs(result.Node, tree.Root)
            self.assertFalse(tree.AddKeyValue(key, value_from_key(key)))
            self.assertEqual(count_nodes_in_tree(tree), i + 1)

    def test_find_min_max_basic(self):
        tree = BST(None)
        self.assertIsNone(tree.FinMinMax(tree.Root, True))
        self.assertIsNone(tree.FinMinMax(tree.Root, False))
        tree.AddKeyValue(0, 0)
        result = tree.FinMinMax(tree.Root, True)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 0)
        result = tree.FinMinMax(tree.Root, False)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 0)

    def test_find_min_max(self):
        tree = BST(None)
        keys = [10, 5, 15, 3, 7, 12, 16]
        for key in keys:
            tree.AddKeyValue(key, value_from_key(key))
        result = tree.FinMinMax(tree.Root, True)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 16)
        result = tree.FinMinMax(tree.Root, False)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 3)
        left_subtree_root = tree.FindNodeByKey(5).Node
        result = tree.FinMinMax(left_subtree_root, True)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 7)
        result = tree.FinMinMax(left_subtree_root, False)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 3)
        right_subtree_root = tree.FindNodeByKey(15).Node
        result = tree.FinMinMax(right_subtree_root, True)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 16)
        result = tree.FinMinMax(right_subtree_root, False)
        self.assertIsNotNone(result)
        self.assertEqual(result.NodeKey, 12)

    def test_delete_node_by_key_small_tree(self):
        tree = BST(None)
        keys = [10, 5, 15, 3, 7, 12, 16, 9, 8, 6, 17, 11]
        for key in keys:
            tree.AddKeyValue(key, value_from_key(key))
        self.assertFalse(tree.DeleteNodeByKey(-1))
        self.assertEqual(count_nodes_in_tree(tree), len(keys))
        self.assertTrue(tree.DeleteNodeByKey(7))
        result = tree.FindNodeByKey(7)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 1)
        five_node = tree.Root.LeftChild
        replacement = five_node.RightChild
        self.assertIs(replacement.Parent, five_node)
        self.assertEqual(replacement.NodeKey, 8)
        self.assertIsNotNone(replacement.LeftChild)
        self.assertEqual(replacement.LeftChild.NodeKey, 6)
        self.assertIsNotNone(replacement.RightChild)
        self.assertEqual(replacement.RightChild.NodeKey, 9)
        self.assertIs(replacement.RightChild.Parent, replacement)
        self.assertIs(replacement.LeftChild.Parent, replacement)
        self.assertTrue(tree.DeleteNodeByKey(3))
        result = tree.FindNodeByKey(3)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 2)
        self.assertIsNone(five_node.LeftChild)
        fifteen_node = tree.Root.RightChild
        self.assertTrue(tree.DeleteNodeByKey(12))
        result = tree.FindNodeByKey(12)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 3)
        self.assertEqual(fifteen_node.LeftChild.NodeKey, 11)
        self.assertIs(fifteen_node.LeftChild.Parent, fifteen_node)
        self.assertIsNone(fifteen_node.LeftChild.LeftChild)
        self.assertIsNone(fifteen_node.LeftChild.RightChild)
        self.assertTrue(tree.DeleteNodeByKey(16))
        result = tree.FindNodeByKey(16)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 4)
        self.assertEqual(fifteen_node.RightChild.NodeKey, 17)
        self.assertIs(fifteen_node.RightChild.Parent, fifteen_node)
        self.assertIsNone(fifteen_node.RightChild.LeftChild)
        self.assertIsNone(fifteen_node.RightChild.RightChild)

    def test_delete_root_basic(self):
        tree = BST(None)
        keys = [1, 0, 2]
        for key in keys:
            tree.AddKeyValue(key, value_from_key(key))
        self.assertTrue(tree.DeleteNodeByKey(1))
        result = tree.FindNodeByKey(1)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 1)

    def test_delete_root(self):
        tree = BST(None)
        keys = [10, 5, 15, 3, 7, 12, 16, 9, 8, 6, 17, 11]
        for key in keys:
            tree.AddKeyValue(key, value_from_key(key))
        self.assertTrue(tree.DeleteNodeByKey(10))
        result = tree.FindNodeByKey(10)
        self.assertIsNotNone(result.Node)
        self.assertFalse(result.NodeHasKey)
        self.assertEqual(count_nodes_in_tree(tree), len(keys) - 1)

    def test_empty_and_single_node_count(self):
        tree = BST(None)
        self.assertEqual(tree.Count(), 0)
        tree = BST(BSTNode(0, 0, None))
        self.assertEqual(tree.Count(), 1)

    def test_fully_delete_tree_and_check_count_in_process(self):
        tree = BST(None)
        keys = list(range(3))
        shuffle(keys)
        for i, key in enumerate(keys):
            self.assertTrue(tree.AddKeyValue(key, value_from_key(key)))
            self.assertEqual(tree.Count(), i + 1)
            self.assertEqual(tree.Count(), count_nodes_in_tree(tree))
        shuffle(keys)
        for i, key in enumerate(keys):
            self.assertTrue(tree.DeleteNodeByKey(key))
            self.assertEqual(tree.Count(), count_nodes_in_tree(tree))
            self.assertEqual(count_nodes_in_tree(tree), len(keys) - (i + 1))
            self.assertEqual(tree.Count(), len(keys) - (i + 1))


if __name__ == '__main__':
    unittest.main()
