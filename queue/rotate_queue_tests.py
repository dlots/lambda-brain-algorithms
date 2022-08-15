import unittest
from queue import Queue
from rotate_queue import rotate_queue


class TestRotateQueue(unittest.TestCase):
    def test_rotate_queue(self):
        queue = Queue()
        for i in range(1, 101):
            queue.enqueue(i)
        rotate_queue(queue, 20)
        self.assertEqual(queue.dequeue(), 21)
        rotate_queue(queue, 79)
        self.assertEqual(queue.dequeue(), 1)


if __name__ == '__main__':
    unittest.main()
