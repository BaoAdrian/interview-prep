"""
LeetCode: Valid Parentheses (#53)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing 
at least one number) which has the largest sum and return its sum.

NOTE
- At each step, it decides to store either the current running max (max 
plus current element) OR just the current element if it is creater than
the evaluated some previously calculated.
"""

def max_sub_array(nums):
    running_max = 0
    max_subarrays = []
    for num in nums:
        new_max = max(num, running_max + num)
        running_max = new_max
        max_subarrays.append(new_max)
        
    return max(max_subarrays)

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("Arr: {}\nMax: {}\n".format(nums, max_sub_array(nums)))

    nums = [1]
    print("Arr: {}\nMax: {}\n".format(nums, max_sub_array(nums)))

    nums = [-2,1,-3,4,4,4,4,-5,4]
    print("Arr: {}\nMax: {}\n".format(nums, max_sub_array(nums)))

if __name__ == "__main__":
    main()