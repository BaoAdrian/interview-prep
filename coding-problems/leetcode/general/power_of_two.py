"""
Power of Two (#231)
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time: 28ms (90.27%)
        Mem:  12.8 MB (100%)
        """
        curr = 1 # Edge case, start at 1
        exp = 0
        while curr < n:
            curr = math.pow(2, exp)
            exp += 1
        
        if curr == n:
            return True
        return False