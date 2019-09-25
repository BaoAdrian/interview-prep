"""
Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum 
of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        return self.smarter_dfs(root, L, R, [])
    
    def dfs(self, node, L, R, total):
        if node.val >= L and node.val <= R:
            total.append(node.val)
        self.dfs(node.left, L, R, total) if node.left else None
        self.dfs(node.right, L, R, total) if node.right else None
    
        return sum(total)
    
    def smarter_dfs(self, node, L, R, total):
        if node == None:
            return
        
        if node.val >= L and node.val <= R:
            total.append(node.val)
            
        if node.val <= L:
            self.smarter_dfs(node.right, L, R, total)
        elif node.val >= R:
            self.smarter_dfs(node.left, L, R, total)
        else:
            self.smarter_dfs(node.left, L, R, total)
            self.smarter_dfs(node.right, L, R, total)
        
        return sum(total)