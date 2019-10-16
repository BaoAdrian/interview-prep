"""
Backspace String Comparison
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are 
typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack, t_stack = [], []
        for s in S:
            if s != '#':
                s_stack.append(s)
            else:
                s_stack.pop() if s_stack else None
                      
        for t in T:
            if t != '#':
                t_stack.append(t)
            else:
                t_stack.pop() if t_stack else None
        
        return s_stack == t_stack