"""
Construct binary tree from preorder/inorder traversals
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Time: 148ms - 53.72%
    Space: 52.9MB - 34.21%
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            val = preorder.pop(0)
            idx = inorder.index(val)
            root = TreeNode(val)
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root