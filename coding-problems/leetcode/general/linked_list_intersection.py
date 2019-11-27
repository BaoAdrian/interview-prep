
"""
Intersection of Two Linked Lists (#160)
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at 
which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Time: 156ms (92.41%)
        Mem: 28.9MB (100%)
        """
        nodes = {}
        
        currA = headA
        # Add nodes in list A
        while currA:
            if currA not in nodes:
                nodes[currA] = 1
            currA = currA.next
            
        # Traverse B until intersection occurs
        currB = headB
        while currB:
            if currB not in nodes:
                nodes[currB] = 1
            else:
                return currB
            currB = currB.next
        return None