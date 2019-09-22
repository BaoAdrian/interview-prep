from tree import *
import unittest

class TestTree(unittest.TestCase):
    def test_insert(self):
        root = BSTNode(10)
        expected_str = "(None < 10 > None)"
        self.assertEqual(str(root), expected_str)
        root.insert(BSTNode(5))
        root.insert(BSTNode(15))
        expected_str = "((None < 5 > None) < 10 > (None < 15 > None))"
        self.assertEqual(str(root), expected_str)
        self.assertTrue(root)
        self.assertTrue(10 in root)
        self.assertTrue(5 in root)
        self.assertTrue(15 in root)

    def test_remove(self):
        root = BSTNode(10)
        root.insert(BSTNode(5))
        root.insert(BSTNode(15))
        self.assertTrue(5 in root)
        self.assertTrue(10 in root)
        self.assertTrue(15 in root)
        root.remove(15)
        self.assertFalse(15 in root)
        expected_str = "((None < 5 > None) < 10 > None)"
        self.assertEqual(str(root), expected_str)
        invalid_node = root.remove(999)
        self.assertTrue(invalid_node == None)
        self.assertFalse(999 in root)

    def test_search(self):
        root = BSTNode(10)
        root.insert(BSTNode(5))
        root.insert(BSTNode(15))
        root.insert(BSTNode(8))
        root.insert(BSTNode(12))
        self.assertTrue(5 in root)
        self.assertTrue(8 in root)
        self.assertTrue(10 in root)
        self.assertTrue(12 in root)
        self.assertTrue(15 in root)
        self.assertTrue(root.search(12))
        self.assertFalse(root.search(999))

    def test_traversals(self):
        root = BSTNode(10)
        root.insert(BSTNode(5))
        root.insert(BSTNode(15))
        root.insert(BSTNode(8))
        root.insert(BSTNode(12))
        expected_preorder = [10,5,8,15,12]
        expected_inorder = [5,8,10,12,15]
        expected_postorder = [8,5,12,15,10]
        self.assertEqual(root.preorder_traversal([]), expected_preorder)
        self.assertEqual(root.inorder_traversal([]), expected_inorder)
        self.assertEqual(root.postorder_traversal([]), expected_postorder)

    def test_height(self):
        root = BSTNode(10)
        root.insert(BSTNode(5))
        root.insert(BSTNode(15))
        self.assertEqual(root.get_height(), 2)
        root.insert(BSTNode(8))
        self.assertEqual(root.get_height(), 3)
        root.insert(BSTNode(12))
        self.assertEqual(root.get_height(), 3)
        root.insert(BSTNode(11))
        self.assertEqual(root.get_height(), 4)
        root.insert(BSTNode(20))
        self.assertEqual(root.get_height(), 4)
        root.remove(11)
        self.assertEqual(root.get_height(), 3)

if __name__ == "__main__":
    unittest.main()