"""
Max Depth
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(max_height(root.left, 1), max_height(root.right, 1))
    
def max_height(node, height):
    if not node:
        return 1
    return 1 + max(max_height(node.left, height), max_height(node.right, height))