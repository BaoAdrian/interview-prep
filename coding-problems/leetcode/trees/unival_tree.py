# https://leetcode.com/problems/univalued-binary-tree/
#A binary tree is univalued if every node in the tree has the same value.

#Return true if and only if the given tree is univalued.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isUnivalTree(self, root):
        """
        Cleaner Solution
        Time: 12ms (94.56%)
        Space: 11.9MB (16.67%)
        """
        if not root:
            return True
        else:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None or (root.right is None and root.left is None):
            return True
        if root.right is not None and root.left is None:
            equal = root.val == root.right.val
            return equal and self.isUnivalTree(root.right)
        if root.left is not None and root.right is None:
            equal = root.val == root.left.val
            return equal and self.isUnivalTree(root.left)
        else:
            equal = root.val == root.left.val == root.right.val
            return equal and self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
