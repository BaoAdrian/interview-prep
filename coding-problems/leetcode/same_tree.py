"""
Same Trees

Description: Given two binary trees, write a function to check
if they are the same or not. 
Two binary trees are considered the same if they are structurally 
identical and the nodes have the same value.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """ Call recursive preorder traversal function and compare """
        path_p = preorder(p, [])
        path_q = preorder(q, [])
        return path_p == path_q
        
def preorder(root, path):
    if not root:
        path.append(None)
        return
    else:
        path.append(root.val)
        preorder(root.left, path)
        preorder(root.right, path)
    return path