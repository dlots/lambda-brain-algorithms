import unittest
from time import time
from set import PowerSet


class TestSet(unittest.TestCase):
    def test_put_new(self):
        p_set = PowerSet()
        for i in range(1, 1001):
            p_set.put(i)
            self.assertEqual(p_set.size(), i)
            self.assertTrue(i in p_set.storage)

    def test_put_existing(self):
        p_set = PowerSet()
        for i in range(1, 1001):
            p_set.put(i)
            self.assertEqual(p_set.size(), i)
            self.assertTrue(p_set.get(i))
        for i in range(1, 1001):
            p_set.put(i)
            self.assertEqual(p_set.size(), 1000)
            self.assertEqual(len([value for value in p_set.storage if value == i]), 1)

    def test_remove_existing(self):
        p_set = PowerSet()
        for i in range(1, 1001):
            p_set.put(i)
        self.assertTrue(p_set.remove(500))
        self.assertEqual(p_set.size(), 999)
        self.assertFalse(p_set.get(500))

    def test_remove_non_existing(self):
        p_set = PowerSet()
        for i in range(1, 1001):
            p_set.put(i)
        self.assertFalse(p_set.remove(1001))
        self.assertEqual(p_set.size(), 1000)
        self.assertFalse(p_set.get(1001))

    def test_intersection_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(1001, 2001):
            p_set2.put(i)
        self.assertEqual(p_set1.intersection(p_set2).size(), 0)

    def test_intersection_not_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(501, 1501):
            p_set2.put(i)
        self.assertEqual(p_set1.intersection(p_set2).size(), 500)

    def test_union_intersecting(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(501, 1501):
            p_set2.put(i)
        self.assertEqual(p_set1.union(p_set2).size(), 1500)

    def test_union_non_intersecting(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(1001, 1501):
            p_set2.put(i)
        self.assertEqual(p_set1.union(p_set2).size(), 1500)

    def test_union_self_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1001, 1501):
            p_set2.put(i)
        self.assertEqual(p_set1.union(p_set2).size(), 500)

    def test_union_param_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        self.assertEqual(p_set1.union(p_set2).size(), 1000)

    def test_difference_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(1, 1001):
            p_set2.put(i)
        self.assertEqual(p_set1.difference(p_set2).size(), 0)

    def test_difference_not_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(501, 1001):
            p_set2.put(i)
        self.assertEqual(p_set1.difference(p_set2).size(), 500)

    def test_issubset_param_in_self(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(501, 1001):
            p_set2.put(i)
        self.assertTrue(p_set1.issubset(p_set2))

    def test_issubset_self_in_param(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(501, 1001):
            p_set1.put(i)
        for i in range(1, 1001):
            p_set2.put(i)
        self.assertFalse(p_set1.issubset(p_set2))

    def test_issubset_intersecting(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 1001):
            p_set1.put(i)
        for i in range(501, 1501):
            p_set2.put(i)
        self.assertFalse(p_set1.issubset(p_set2))

    def test_issubset_both_empty(self):
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        self.assertTrue(p_set1.issubset(p_set2))

    def test_speed(self):
        max_time = 2
        p_set1 = PowerSet()
        p_set2 = PowerSet()
        for i in range(1, 20001):
            p_set1.put(i)
        for i in range(1, 20001):
            p_set2.put(i)
        start = time()
        p_set1.put(20001)
        self.assertLess(time() - start, max_time)
        self.assertEqual(p_set1.size(), 20001)
        start = time()
        p_set1.remove(20001)
        self.assertLess(time() - start, max_time)
        self.assertEqual(p_set1.size(), 20000)
        start = time()
        p_set1.intersection(p_set2)
        self.assertLess(time() - start, max_time)
        start = time()
        p_set1.union(p_set2)
        self.assertLess(time() - start, max_time)
        start = time()
        p_set1.difference(p_set2)
        self.assertLess(time() - start, max_time)
        start = time()
        p_set1.issubset(p_set2)
        self.assertLess(time() - start, max_time)


if __name__ == '__main__':
    unittest.main()
