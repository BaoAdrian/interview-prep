from stack import *
import unittest

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.is_empty())
        self.assertTrue(1 in stack)
        self.assertTrue(2 in stack)
        self.assertTrue(3 in stack)
        self.assertEqual(len(stack), 3)
    
    def test_pop(self):
        stack = Stack()
        stack.push(100)
        stack.push(200)
        self.assertEqual(len(stack), 2)
        self.assertTrue(200 in stack)
        self.assertEqual(200, stack.pop())
        self.assertFalse(200 in stack)

    def test_peek(self):
        stack = Stack()
        stack.push("Botttom")
        stack.push("Middle")
        stack.push("Top")
        self.assertEqual(len(stack), 3)
        self.assertEqual("Top", stack.peek())
        self.assertNotEqual("Bottom", stack.peek())

    def test_search(self):
        stack = Stack()
        stack.push(1)
        stack.push("middle")
        stack.push(3000)
        stack.push("top")
        self.assertEqual(len(stack), 4)
        self.assertEqual(3000, stack.search_and_remove(3000))
        self.assertEqual(None, stack.search_and_remove(999))

if __name__ == "__main__":
    unittest.main()
    