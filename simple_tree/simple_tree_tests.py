import unittest
from simple_tree import SimpleTree, SimpleTreeNode


def make_tree():
    return SimpleTree(SimpleTreeNode(0, None))


class TestSimpleTree(unittest.TestCase):
    def testAddChild(self):
        tree = make_tree()
        self.assertEqual(len(tree.FindNodesByValue(1)), 0)
        tree.AddChild(tree.Root, SimpleTreeNode(1, tree.Root))
        self.assertEqual(len(tree.FindNodesByValue(1)), 1)

    def testDeleteNode(self):
        tree = make_tree()
        new_node = SimpleTreeNode(1, tree.Root)
        tree.AddChild(tree.Root, new_node)
        tree.AddChild(new_node, SimpleTreeNode(2, new_node))
        self.assertEqual(len(tree.FindNodesByValue(1)), 1)
        self.assertEqual(len(tree.FindNodesByValue(2)), 1)
        tree.DeleteNode(new_node)
        self.assertEqual(len(tree.FindNodesByValue(1)), 0)
        self.assertEqual(len(tree.FindNodesByValue(2)), 0)

    def testGetAllNodes(self):
        tree = make_tree()
        new_nodes = [SimpleTreeNode(1, tree.Root)]
        tree.AddChild(tree.Root, new_nodes[0])
        new_nodes.append(SimpleTreeNode(2, tree.Root))
        tree.AddChild(new_nodes[0], new_nodes[1])
        all_nodes = tree.GetAllNodes()
        for new_node in new_nodes:
            self.assertIn(new_node, all_nodes)

    def testFindNodesByValue(self):
        tree = make_tree()
        for _ in range(50):
            tree.AddChild(tree.Root, SimpleTreeNode(1, tree.Root))
        for node in tree.GetAllNodes():
            tree.AddChild(node, SimpleTreeNode(2, node))
        ones = tree.FindNodesByValue(1)
        self.assertEqual(len(ones), 50)
        twos = tree.FindNodesByValue(2)
        self.assertEqual(len(twos), 51)
        for two in twos:
            self.assertTrue(two.Parent is tree.Root or two.Parent in ones)

    def testMoveNode(self):
        tree = make_tree()
        new_parent = SimpleTreeNode(1, tree.Root)
        moved_node = SimpleTreeNode(2, tree.Root)
        tree.AddChild(tree.Root, new_parent)
        tree.AddChild(tree.Root, moved_node)
        tree.MoveNode(moved_node, new_parent)
        self.assertNotIn(moved_node, tree.Root.Children)
        self.assertIn(moved_node, new_parent.Children)
        self.assertIs(moved_node.Parent, new_parent)

    def testCount(self):
        tree = make_tree()
        for _ in range(50):
            tree.AddChild(tree.Root, SimpleTreeNode(1, tree.Root))
        for node in tree.GetAllNodes():
            tree.AddChild(node, SimpleTreeNode(2, node))
        self.assertEqual(tree.Count(), 102)

    def testLeafCount(self):
        tree = make_tree()
        for _ in range(50):
            tree.AddChild(tree.Root, SimpleTreeNode(1, tree.Root))
        for node in tree.GetAllNodes():
            tree.AddChild(node, SimpleTreeNode(2, node))
        self.assertEqual(tree.LeafCount(), 51)


if __name__ == '__main__':
    unittest.main()
