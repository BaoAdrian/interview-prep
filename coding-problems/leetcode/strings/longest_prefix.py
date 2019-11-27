"""
Longest Common Prefix (#14)
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time: 24ms (99.34%)
        Mem: 12.8MB (100%)
        """
        if not strs:
            return ""
        
        min_len = min([len(s) for s in strs])
        longest_prefix = ""
        for i in range(min_len):
            curr = strs[0][i]
            for str in strs:
                if str[i] != curr:
                    return longest_prefix
            longest_prefix += curr
        return longest_prefix