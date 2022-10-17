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
        for _ in range(50):
            tree.AddChild(tree.Root, SimpleTreeNode(1, tree.Root))
        for node in tree.GetAllNodes():
            tree.AddChild(node, SimpleTreeNode(2, node))
        self.assertEqual(tree.Count(), 102)
        tree.DeleteNode(tree.Root.Children[0])
        self.assertEqual(tree.Count(), 100)
        new_root = SimpleTreeNode(-1, None)
        old_root = tree.Root
        tree.Root = new_root
        tree.AddChild(tree.Root, old_root)
        tree.DeleteNode(tree.Root.Children[0])
        self.assertEqual(tree.Count(), 1)

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

    def testEvenTrees(self):
        one = SimpleTreeNode(1, None)
        tree = SimpleTree(one)
        two = SimpleTreeNode(2, None)
        three = SimpleTreeNode(3, None)
        six = SimpleTreeNode(6, None)
        tree.AddChild(one, two)
        tree.AddChild(one, three)
        tree.AddChild(one, six)
        five = SimpleTreeNode(5, None)
        seven = SimpleTreeNode(7, None)
        tree.AddChild(two, five)
        tree.AddChild(two, seven)
        four = SimpleTreeNode(4, None)
        tree.AddChild(three, four)
        eight = SimpleTreeNode(8, None)
        tree.AddChild(six, eight)
        nine = SimpleTreeNode(9, None)
        ten = SimpleTreeNode(10, None)
        tree.AddChild(eight, nine)
        tree.AddChild(eight, ten)
        result = tree.EvenTrees()
        self.assertTrue(result == [one, three, one, six] or result == [one, six, one, three])


if __name__ == '__main__':
    unittest.main()
