import unittest
from random import sample
from collections import deque
from balanced_bst import BalancedBST
from array_binary_search_tree.array_binary_search_tree import get_tree_size_from_depth



class MyTestCase(unittest.TestCase):
    def test_generate_balanced_bst(self):
        array = [43, 12, 22, 0, 46, 21, 100]
        tree = BalancedBST()
        tree.GenerateTree(array)
        self.assertTrue(tree.IsBalanced(tree.Root))
        queue = deque()
        queue.appendleft((tree.Root, 0, None))
        while len(queue) > 0:
            node, expected_level, expected_parent = queue.pop()
            self.assertEqual(node.Level, expected_level)
            self.assertIs(node.Parent, expected_parent)
            if expected_parent is not None and node is expected_parent.LeftChild:
                self.assertLess(node.NodeKey, expected_parent.NodeKey)
            if expected_parent is not None and node is expected_parent.RightChild:
                self.assertGreater(node.NodeKey, expected_parent.NodeKey)
            if node.LeftChild is not None:
                queue.appendleft((node.LeftChild, expected_level + 1, node))
            if node.RightChild is not None:
                queue.appendleft((node.RightChild, expected_level + 1, node))

    def test_tree_is_not_balanced(self):
        array = [43, 12, 22, 0, 46, 21, 100]
        tree = BalancedBST()
        tree.GenerateTree(array)
        tree.Root.RightChild = None
        self.assertFalse(tree.IsBalanced(tree.Root))

    def test_generate_balanced_bst_array_randomized(self):
        for depth in range(10):
            size = get_tree_size_from_depth(depth)
            array = sample(range(10000), size)
            tree = BalancedBST()
            tree.GenerateTree(array)
            self.assertTrue(tree.IsBalanced(tree.Root))
            queue = deque()
            queue.appendleft((tree.Root, 0, None))
            while len(queue) > 0:
                node, expected_level, expected_parent = queue.pop()
                self.assertEqual(node.Level, expected_level)
                self.assertIs(node.Parent, expected_parent)
                if expected_parent is not None and node is expected_parent.LeftChild:
                    self.assertLess(node.NodeKey, expected_parent.NodeKey)
                if expected_parent is not None and node is expected_parent.RightChild:
                    self.assertGreater(node.NodeKey, expected_parent.NodeKey)
                if node.LeftChild is not None:
                    queue.appendleft((node.LeftChild, expected_level + 1, node))
                if node.RightChild is not None:
                    queue.appendleft((node.RightChild, expected_level + 1, node))


if __name__ == '__main__':
    unittest.main()
