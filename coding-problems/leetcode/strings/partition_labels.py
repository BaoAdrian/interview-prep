"""
Parition Labels (#763)
https://leetcode.com/problems/partition-labels/

A string S of lowercase letters is given. We want to 
partition this string into as many parts as possible so 
that each letter appears in at most one part, and return a
 list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        Time: 36ms (95.15%)
        Mem: 12.8MB (100%)
        """
        # Build map of last occurrences
        last_occur = {}
        for i in range(len(S)):
            last_occur[S[i]] = i
            
        output = []
        max_last = -1
        for i in range(len(S)):
            max_last = max(max_last, last_occur[S[i]])
            
            if i == max_last:
                # Partition
                output.append(i + 1 - sum(output))

        return output