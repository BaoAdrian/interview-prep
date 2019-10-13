"""
Find and Replace pattern
https://leetcode.com/problems/find-and-replace-pattern/

You have a list of words and a pattern, and you want to know which words in 
words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that 
after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: 
every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
"""


def findAndReplacePattern(self, words, pattern):
    """
    Time:  28 ms  (99.67%)
    Space: 13.9MB (11.11%)
    """
    res = []
    
    def match(word, pattern):
        if len(word) != len(pattern):
            return False
        dir = {}
        for w, p in zip(word, pattern):
            if w not in dir:
                if p in dir.values():
                    return False
                dir[w] = p
            else:
                if dir[w] != p:
                    return False
        return True
                   
    for w in words:
        if match(w, pattern):
            res.append(w)
    return res




class Solution:
    """
    This solution finds ALL possible permutated patterns as opposed to the 
    strict ordering requested by the original problem (solved above)
    """
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        target = {}
        for c in pattern:
            if c not in target:
                target[c] = 0
            target[c] += 1
            
        matches = []
        for word in words:
            map = {}
            for c in word:
                if c not in map:
                    map[c] = 0
                map[c] += 1
            if len(map) == len(target) and sum(map.values()) == sum(target.values()):
                matches.append(word)
        return matches