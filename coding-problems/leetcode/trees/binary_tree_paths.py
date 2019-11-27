"""
Binary Tree Paths (#257)
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        Time: 32ms (88.09%)
        Mem: 12.7MB (100%)
        """
        if not root:
            return []
        return self.dfs(root, "", [])
    
    def dfs(self, root, curr_path, paths):
        curr_path += str(root.val)
        
        if not root.left and not root.right:
            # Leaf reached
            paths.append(curr_path)
            return paths
        
        self.dfs(root.left, curr_path + "->", paths) if root.left else None
        self.dfs(root.right, curr_path+ "->", paths) if root.right else None
            
        return paths