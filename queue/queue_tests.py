import unittest
from queue import Queue
from two_stacks_queue import StackBasedQueue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queues = [Queue(), StackBasedQueue()]
        for queue in queues:
            for i in range(1, 101):
                queue.enqueue(i)
                self.assertEqual(queue.size(), i)
            self.assertEqual(queue.dequeue(), 1)

    def test_dequeue(self):
        queues = [Queue(), StackBasedQueue()]
        for queue in queues:
            self.assertIsNone(queue.dequeue())
            for i in range(1, 101):
                queue.enqueue(i)
            for i in range(1, 101):
                self.assertEqual(queue.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
