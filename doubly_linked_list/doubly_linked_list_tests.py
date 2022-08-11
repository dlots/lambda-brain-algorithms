import unittest
from doubly_linked_list import LinkedList2, Node


def create_linked_list_from_values(*values):
    linked_list = LinkedList2()
    for value in values:
        linked_list.add_in_tail(Node(value))
    return linked_list


class LinkedListTests(unittest.TestCase):
    def test_empty_list_deletion_(self):
        linked_list = LinkedList2()
        linked_list.delete(0, False)
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        linked_list.delete(0, True)
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_single_item_single_deletion_(self):
        linked_list = create_linked_list_from_values(0)
        linked_list.delete(1, False)
        self.assertEqual(linked_list.len(), 1)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        linked_list.delete(0, False)
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_single_item_multiple_deletion_(self):
        linked_list = create_linked_list_from_values(0)
        linked_list.delete(1, True)
        self.assertEqual(linked_list.len(), 1)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        linked_list.delete(0, True)
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_multiple_items_single_deletion_(self):
        linked_list = create_linked_list_from_values(0, 2, 0, 0, 0, 2)
        linked_list.delete(1, False)
        self.assertEqual(linked_list.len(), 6)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 2)
        linked_list.delete(0, False)
        self.assertEqual(linked_list.len(), 5)
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 2)

        linked_list = create_linked_list_from_values(1, 1, 1, 1, 2, 0)
        linked_list.delete(0, False)
        self.assertEqual(linked_list.len(), 5)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 2)

    def test_multiple_items_multiple_deletion_(self):
        linked_list = create_linked_list_from_values(0, 2, 0, 0, 3, 0)
        linked_list.delete(1, True)
        self.assertEqual(linked_list.len(), 6)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        linked_list.delete(0, True)
        self.assertEqual(linked_list.len(), 2)
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.tail.value, 3)

    def test_list_clean(self):
        linked_list = create_linked_list_from_values()
        linked_list.clean()
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        linked_list = create_linked_list_from_values(0)
        linked_list.clean()
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        linked_list = create_linked_list_from_values(0, 0, 0, 0, 0, 0, 0)
        linked_list.clean()
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_list_find_all(self):
        self.assertEqual(len(LinkedList2().find_all(0)), 0)
        self.assertEqual(len(create_linked_list_from_values(1).find_all(0)), 0)
        self.assertEqual(len(create_linked_list_from_values(0).find_all(0)), 1)
        self.assertEqual(len(create_linked_list_from_values(1, 2, 3).find_all(0)), 0)
        self.assertEqual(len(create_linked_list_from_values(0, 1, 2).find_all(0)), 1)
        self.assertEqual(len(create_linked_list_from_values(0, 1, 0, 2, 0, 0).find_all(0)), 4)

    def test_list_len(self):
        linked_list = LinkedList2()
        self.assertEqual(linked_list.len(), 0)
        linked_list.delete(3, False)
        self.assertEqual(linked_list.len(), 0)
        linked_list = create_linked_list_from_values(0)
        self.assertEqual(linked_list.len(), 1)
        linked_list = create_linked_list_from_values(0, 0)
        self.assertEqual(linked_list.len(), 2)
        linked_list.add_in_tail(Node(1))
        self.assertEqual(linked_list.len(), 3)
        linked_list.delete(0, True)
        self.assertEqual(linked_list.len(), 1)

    def test_list_insertion(self):
        linked_list = LinkedList2()
        node1 = Node(1)
        linked_list.insert(None, node1)
        self.assertEqual(linked_list.len(), 1)
        self.assertIs(linked_list.head, node1)
        self.assertIs(linked_list.tail, node1)
        node2 = Node(2)
        linked_list.insert(node1, node2)
        self.assertEqual(linked_list.len(), 2)
        self.assertIs(linked_list.head, node1)
        self.assertIs(linked_list.tail, node2)
        node3 = Node(3)
        linked_list.insert(None, node3)
        self.assertEqual(linked_list.len(), 3)
        self.assertIs(linked_list.head, node1)
        self.assertIs(linked_list.tail, node3)
        node4 = Node(4)
        linked_list.insert(node2, node4)
        self.assertEqual(linked_list.len(), 4)
        self.assertIs(linked_list.head, node1)
        self.assertIs(linked_list.tail, node3)


if __name__ == '__main__':
    unittest.main()
