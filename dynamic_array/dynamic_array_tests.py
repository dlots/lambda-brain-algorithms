import unittest
from dynamic_array import DynArray


class MyTestCase(unittest.TestCase):
    def test_insertion_within_capacity(self):
        array = DynArray()
        count = array.count
        for i in range(array.minimal_capacity):
            array.insert(0, i)
            self.assertEqual(array.capacity, array.minimal_capacity)
            self.assertEqual(array[0], i)
            count += 1
            self.assertEqual(array.count, count)

    def test_insertion_exceeding_capacity(self):
        array = DynArray()
        count = array.count
        for i in range(array.minimal_capacity):
            count += 1
            array.append(i)
        array.insert(0, 123)
        self.assertEqual(array.capacity, 2 * array.minimal_capacity)
        self.assertEqual(array[0], 123)
        self.assertEqual(array.count, count + 1)

    def test_out_of_bound_insertion(self):
        array = DynArray()
        with self.assertRaises(IndexError):
            array.insert(-1, 1)
        self.assertEqual(array.count, 0)
        with self.assertRaises(IndexError):
            array.insert(1, 1)
        self.assertEqual(array.count, 0)
        array.append(1)
        with self.assertRaises(IndexError):
            array.insert(2, 1)
        self.assertEqual(array.count, 1)

    def test_deletion_no_resize(self):
        array = DynArray()
        for i in range(32):
            array.append(i)
        self.assertEqual(array.count, 32)
        self.assertEqual(array.capacity, 32)
        array.delete(0)
        self.assertEqual(array.count, 31)
        self.assertEqual(array.capacity, 32)
        self.assertEqual(array[0], 1)

    def test_deletion_with_resize(self):
        array = DynArray()
        for i in range(17):
            array.append(i)
        self.assertEqual(array.count, 17)
        self.assertEqual(array.capacity, 32)
        array.delete(0)
        array.delete(0)
        self.assertEqual(array.count, 15)
        self.assertEqual(array.capacity, 21)
        self.assertEqual(array[0], 2)

    def test_out_of_bounds_deletion(self):
        array = DynArray()
        with self.assertRaises(IndexError):
            array.delete(-1)
        with self.assertRaises(IndexError):
            array.delete(0)
        array.append(0)
        with self.assertRaises(IndexError):
            array.delete(1)


if __name__ == '__main__':
    unittest.main()
