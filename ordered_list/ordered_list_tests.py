import unittest
from ordered_list import OrderedList


class TestOrderedList(unittest.TestCase):
    def test_add_ascending(self):
        o_list = OrderedList(True)
        nums = [23, 532, 13, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
            self.assertEqual(o_list.len(), i + 1)
            to_list = [node.value for node in o_list.get_all()]
            self.assertTrue(num in to_list)
            for j in range(o_list.len() - 1):
                self.assertTrue(to_list[j] <= to_list[j + 1])

    def test_add_descending(self):
        o_list = OrderedList(False)
        nums = [23, 532, 13, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
            self.assertEqual(o_list.len(), i + 1)
            to_list = [node.value for node in o_list.get_all()]
            self.assertTrue(num in to_list)
            for j in range(o_list.len() - 1):
                self.assertTrue(to_list[j] >= to_list[j + 1])

    def test_delete_ascending(self):
        o_list = OrderedList(True)
        nums = [23, 532, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
        self.assertEqual(o_list.len(), len(nums))
        for i, num in enumerate(nums):
            o_list.delete(num)
            self.assertEqual(o_list.len(), len(nums) - i - 1)
            to_list = [node.value for node in o_list.get_all()]
            self.assertTrue(num not in to_list)
            for j in range(o_list.len() - 1):
                self.assertTrue(to_list[j] <= to_list[j + 1])

    def test_delete_descending(self):
        o_list = OrderedList(False)
        nums = [23, 532, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
        self.assertEqual(o_list.len(), len(nums))
        for i, num in enumerate(nums):
            o_list.delete(num)
            self.assertEqual(o_list.len(), len(nums) - i - 1)
            to_list = [node.value for node in o_list.get_all()]
            self.assertTrue(num not in to_list)
            for j in range(o_list.len() - 1):
                self.assertTrue(to_list[j] >= to_list[j + 1])

    def test_find_ascending(self):
        o_list = OrderedList(True)
        nums = [23, 532, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
        self.assertIsNotNone(o_list.find(12))
        self.assertEqual(o_list.find(6), None)
        self.assertEqual(o_list.find_steps, 4)

    def test_find_descending(self):
        o_list = OrderedList(False)
        nums = [23, 532, 36, 12, 4, 16, 13, 1, 24, 5612, 412, 5]
        for i, num in enumerate(nums):
            o_list.add(num)
        self.assertIsNotNone(o_list.find(12))
        self.assertEqual(o_list.find(6), None)
        self.assertEqual(o_list.find_steps, 10)


if __name__ == '__main__':
    unittest.main()
