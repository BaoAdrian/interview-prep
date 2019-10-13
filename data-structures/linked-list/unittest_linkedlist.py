from linked_list import *
import unittest

class TestLinkedList(unittest.TestCase):
    def test_add(self):
        ll = SinglyLinkedList()
        self.assertTrue(ll.is_empty())
        nodes = [Node(1), Node(2), Node(3)]
        [ll.add(node) for node in nodes]
        self.assertEqual(len(ll), 3)
        self.assertTrue(1 in ll)
        self.assertTrue(2 in ll)
        self.assertTrue(3 in ll)
        self.assertFalse(ll.is_empty())
        self.assertEqual(ll.search(1), 2)
        self.assertEqual(ll.search(2), 1)
        self.assertEqual(ll.search(3), 0)
        ll.append(Node(100))
        self.assertEqual(ll.search(100), 3)
        ll.add(Node(999))
        self.assertEqual(ll.search(999), 0)
        self.assertEqual(ll.search(3), 1)

    def test_remove_by_element(self):
        ll = SinglyLinkedList()
        self.assertTrue(ll.is_empty())
        nodes = [Node(1), Node(2), Node(3)]
        [ll.add(node) for node in nodes]
        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 3)
        ll.remove_by_element(1)
        self.assertEqual(len(ll), 2)
        self.assertFalse(1 in ll)
        ll.remove_by_element(2)
        self.assertEqual(len(ll), 1)
        self.assertFalse(ll.is_empty())
        ll.remove_by_element(3)
        self.assertTrue(ll.is_empty())

    def test_remove_by_index(self):
        ll = SinglyLinkedList()
        self.assertTrue(ll.is_empty())
        nodes = [Node(1), Node(2), Node(3)]
        [ll.add(node) for node in nodes]
        self.assertTrue(1 in ll)
        self.assertEqual(ll.search(1), 2)
        ll.remove_by_index(2)
        self.assertFalse(1 in ll)
        self.assertEqual(ll.search(1), -1)

if __name__ == "__main__":
    unittest.main()