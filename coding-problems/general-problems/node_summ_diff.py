"""
node_sum_diff.py
Given a binary tree, write a recursive function to return the 
difference between the sum of all node values at odd levels and 
sum of all node values at even levels. Define the root node 
to be at level 1. 

Assume you are given the BinNode class below
"""

# class BinNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = left
#         self.right = right
    
#     def value(self):
#         return self.value
    
#     def set_value(self, value):
#         self.value = value

#     def left(self):
#         return self.left

#     def right(self):
#         return self.right

#     def is_leaf(self):
#         return not self.left and not self.right


def bst_sum_diff(root):
    if root == None:
        return 0
    else:
        return root.value() - bst_sum_diff(root.left()) - bst_sum_diff(root.right())
