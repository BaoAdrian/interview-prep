"""
N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.
Given an n-ary tree, return the postorder traversal of its nodes' values.

Note:
Recursive solution is trivial, could you do it iteratively?
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder_iterative(self, root):
        if not root:
            return []
        traversal = []
        stack = [root]
        while stack:

            curr = stack.pop()
            traversal.append(curr.val)

            # Push into stack in reverse order to pop in correct order
            for child in reversed(curr.children):
                stack.append(child)

        return traversal

    def preorder_recursive(self, root: 'Node') -> List[int]:
        return self.preorder_helper(root, [])
    
    def preorder_helper(self, root, traversal):
        if not root:
            return
        else:
            traversal.append(root.val)
            for child in root.children:
                self.preorder_helper(child, traversal)
        return traversal


    def postorder_iterative(self, root: 'Node') -> List[int]:
        if not root:
            return []

        traversal = []
        stack, counters = [root], [0]
        
        while stack:
            while counters[-1] < len(stack[-1].children):
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
            traversal.append(stack.pop().val)
            counters.pop()
            if len(counters) != 0:
                counters[-1] += 1
        return traversal

    def postorder(self, root: 'Node') -> List[int]:
        return self.postorder_helper(root, [])
    
    def postorder_helper(self, root, traversal):
        if not root:
            return
        else:
            for child in root.children:
                self.postorder_helper(child, traversal)
            traversal.append(root.val)
        return traversal