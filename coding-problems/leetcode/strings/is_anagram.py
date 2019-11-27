"""
Valid Anagram (#242)
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine 
if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you 
adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: 48ms (81%)
        Mem: 13.1 (100%)
        """
        s_map = self.build_map(s)
        t_map = self.build_map(t)
        
        if s_map.keys() == t_map.keys() and self.matching_occurrences(s_map, t_map):
            return True
        return False
        
    def build_map(self, s):
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            m[c] += 1
        return m
    
    def matching_occurrences(self, s, t):
        for k,v in s.items():
            if t[k] != v:
                return False
        return True