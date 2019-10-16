"""
Sort Colors
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are 
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the 
color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function 
for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        
        j = 0
        for i in range(len(nums)):
            while counts[j] == 0:
                j += 1
            nums[i] = j
            counts[j] -= 1