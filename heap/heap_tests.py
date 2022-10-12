import unittest
from heap import Heap, get_tree_capacity_from_depth, get_left_child_index, get_right_child_index


def create_heap():
    heap = Heap()
    array = [2, 5, 6, 7, 8, 3, 1, 9, 4, 11, 10, 12, 13, 14, 15]
    depth = 3
    heap.MakeHeap(array, depth)
    return heap, array, depth


def verify_heap_ordering(tests, heap):
    for i, key in enumerate(heap.HeapArray):
        left_child_index = get_left_child_index(i)
        if left_child_index < heap.size:
            tests.assertLess(heap.HeapArray[left_child_index], key)
        right_child_index = get_right_child_index(i)
        if right_child_index < heap.size:
            tests.assertLess(heap.HeapArray[right_child_index], key)


class TestHeap(unittest.TestCase):
    def test_make_heap(self):
        heap, array, depth = create_heap()
        self.assertEqual(heap.size, len(array))
        self.assertEqual(len([key for key in heap.HeapArray if key is not None]), heap.size)
        self.assertEqual(len(heap.HeapArray), get_tree_capacity_from_depth(depth))
        verify_heap_ordering(self, heap)

    def test_get_max_from_heap(self):
        heap, array, _ = create_heap()
        self.assertEqual(heap.GetMax(), max(array))
        self.assertEqual(heap.size, len(array) - 1)
        verify_heap_ordering(self, heap)

    def test_get_max_from_empty_heap(self):
        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)

    def test_add_to_full_heap(self):
        heap, _, _ = create_heap()
        self.assertFalse(heap.Add(100))


if __name__ == '__main__':
    unittest.main()
