"""
Reverese Vowels of String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse 
only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        s = [c for c in s]
        while start < end:
            if self.is_vowel(s[start]) and self.is_vowel(s[end]):
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            else:
                start += 1 if not self.is_vowel(s[start]) else 0
                end -= 1 if not self.is_vowel(s[end]) else 0
        return ''.join(s)
        
    def is_vowel(self, letter):
        """ utility function """
        if letter.lower() in {'a', 'e', 'i', 'o', 'u'}:
            return True
        return False