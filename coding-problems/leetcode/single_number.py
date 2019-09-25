"""
Single Number
https://leetcode.com/problems/single-number/submissions/

Given a non-empty array of integers, every element appears 
twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory.
"""

class Solution:
    def singleNumber(self, nums):
        """ O(n): requires additional space storing cache """
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 0
            cache[num] += 1
        for num, occurrence in cache.items():
            if occurrence != 2:
                return num
        return None

    def singleNumber_noSpace(self, nums):
        """ O(n): No additional space using XOR """
        res = 0
        for num in nums:
            res ^= num
        return res