"""
Invert Tree #226
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

def invertTree(self, root: TreeNode) -> TreeNode:
    """
    Recursive Solution
    Time: 24ms (98.32%)
    Mem: 12.8MB (100.0%)
    """
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
def invertTree(self, root: TreeNode) -> TreeNode:
    """
    BFS
    Time: 28ms (94.33%)
    Mem: 12.5MV (100.0%)
    """
    q = [root]
    while q:
        curr = q.pop(0)
        if curr:
            curr.left, curr.right = curr.right, curr.left
            q.append(curr.left)
            q.append(curr.right)
    return root