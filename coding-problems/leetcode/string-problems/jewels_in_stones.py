"""
Jewels and Stones 
https://leetcode.com/problems/jewels-and-stones/submissions/

You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of 
stone you have.  You want to know how many of the stones you have are 
also jewels.

The letters in J are guaranteed distinct, and all characters in J and S 
are letters. Letters are case sensitive, so "a" is considered a different 
type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # build map
        jewels = {}
        for jewel in S:
            if jewel not in jewels:
                jewels[jewel] = 0
            jewels[jewel] += 1
        
        # Return count of requested jewels
        count = 0
        for req in J:
            if req in jewels:
                count += jewels[req]
        
        return count