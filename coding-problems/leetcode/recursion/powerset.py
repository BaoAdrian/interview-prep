"""
Subsets (#78)
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return 
all possible subsets (the power set).

Note: The solution set must not contain duplicate 
subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: 28ms (97.8%)
        Mem: 13MB (100%)
        """
        if not nums:
            return [[]]
        else:
            subset = []
            for smaller_subset in self.subsets(nums[1:]):
                subset += [smaller_subset]
                subset += [[nums[0]] + smaller_subset]
            return subset