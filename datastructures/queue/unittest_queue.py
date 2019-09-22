from queue import *
import unittest

class TestStack(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(100)
        queue.enqueue(200)
        queue.enqueue(300)
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 3)
        self.assertTrue(100 in queue)
        self.assertTrue(200 in queue)
        self.assertTrue(300 in queue)
        self.assertFalse(999 in queue)
    
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("First in line")
        queue.enqueue("Second in line")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "First in line")
        self.assertEqual(queue.dequeue(), "Second in line")
        self.assertTrue(queue.is_empty())

    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.peek() == 3)
        self.assertFalse(queue.peek() == 2)
        self.assertTrue(queue.peek() == 1)

    def test_remove(self):
        queue = Queue()
        queue.enqueue("One")
        queue.enqueue("Two")
        queue.enqueue("Target")
        queue.enqueue("Three")
        self.assertFalse(queue.is_empty())
        self.assertTrue("Target" in queue)
        self.assertEqual(queue.remove("Target"), "Target")
        self.assertFalse("Target" in queue)
        self.assertEqual(queue.remove("Target"), None)

if __name__ == "__main__":
    unittest.main()
    