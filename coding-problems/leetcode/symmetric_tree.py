"""
Symmetric Trees

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
        1
      /   \
     2     2
    / \   / \
   3   4 4   3 

This binary tree [1,2,2,2,null,2] is not symmetric:
        1
      /   \
     2     2
    /     /
   2     2   
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)
        
def isMirror(left, right):
    """
    is_mirror: This utility function checks the 'reflected'
    position of the tree's left & right side. They must both
    be None OR must have the same value in order to maintain
    symmetric behavior, otherwise, it is not symmetric.
    """
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    
    if left.val == right.val:
        # Recurse through children
        return isMirror(left.left, right.right) and \
                isMirror(left.right, right.left)
    return False