"""
Path Sum (3)
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains 
an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a 
leaf, but it must go downwards (traveling only from parent 
nodes to child nodes).

The tree has no more than 1,000 nodes and the values are 
in the range -1,000,000 to 1,000,000.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.num_paths = 0
        self.dfs(root, sum)
        return self.num_paths
    

    def dfs(self, node, target):
        if node == None:
            return
        else:
            self.crawl_tree(node, target, 0)
            self.dfs(node.left, target)
            self.dfs(node.right, target)

    def crawl_tree(self, node, target, curr_sum):
        if node == None:
            return

        curr_sum += node.val
        if curr_sum == target:
            self.num_paths += 1

        self.crawl_tree(node.left, target, curr_sum)
        self.crawl_tree(node.right, target, curr_sum)