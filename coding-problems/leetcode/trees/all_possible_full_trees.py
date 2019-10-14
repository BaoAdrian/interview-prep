"""
All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

A full binary tree is a binary tree where each node has exactly
 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [
    [0,0,0,null,null,0,0,null,null,0,0],
    [0,0,0,null,null,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,null,null,null,null,0,0],
    [0,0,0,0,0,null,null,0,0]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int, memos={1: [TreeNode(0)]}) -> List[TreeNode]:
        """
        Memoization Solution
        Time: 140ms   (98.81%)
        Space: 16.5MB (42.86%)
        """
        if N in memos: return memos[N]
        ret = []
        for l in range(1, N-1, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        memos[N] = ret
        return ret
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        Recursive Brute Force
        Time: 284ms   (21.05%)
        Space: 27.6MB (14.29%)
        """
        N -= 1
        if N == 0:
            return [TreeNode(0)]
        nodes = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    nodes += [root]
        return nodes
                    