"""
Add Binary
https://leetcode.com/problems/add-binary/submissions/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_out = 0
        i = 0
        running_sum = ""
        a = a[::-1]
        b = b[::-1]
        while i < len(a) and i < len(b):
            sum, carry_out = self.full_adder(a[i], b[i], carry_out)
            running_sum = str(sum) + running_sum
            i += 1
            
        # In the event of uneven numbers, pull remaining values
        while i < len(a):
            sum, carry_out = self.full_adder(a[i], 0, carry_out)
            running_sum = str(sum) + running_sum
            i += 1
        while i < len(b):
            sum, carry_out = self.full_adder(0, b[i], carry_out)
            running_sum = str(sum) + running_sum
            i += 1
        
        # If last addition has carryout, add to the front
        if carry_out:
            running_sum = "1" + running_sum
            
        return running_sum
    
    def full_adder(self, a, b, carry_in):
        a, b = int(a), int(b)
        sum = (a ^ b) ^ carry_in 
        carry_out = (a & b) | ((a ^ b) & carry_in)
        return sum, carry_out