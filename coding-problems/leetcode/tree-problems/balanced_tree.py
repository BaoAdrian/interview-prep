"""
Balanced Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
 > a binary tree in which the depth of the two subtrees of every 
node never differ by more than 1.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_height = get_height(root.left, 1)
        right_height = get_height(root.right, 1)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
def get_height(node, height):
    if node == None:
        return 0
    
    return 1 + max(get_height(node.left, height), (get_height(node.right, height)))