"""
Climbing Stars (#70)
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to 
reach to the top.

Each time you can either climb 1 or 2 steps. In how 
many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time: N/A Time limit exceeded
        Mem: N/A ^
        """
        # Naive solution
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    def climbStairs(self, n):
        """
        Time: 24ms (96.94%)
        Mem:  12.7 MB (100%)
        """
        # DP Solve
        if n == 0 or n == 1:
            return 1
        else:
            # Generate dp array and build as you go
            dp = [0] * (n+1)
            dp[0] = 1
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
                
            return dp[-1]
                
    def climbStairs(self, n):
        """
        Time: 28ms (90.99%)
        Mem: 12.7MB (100%)
        """
        # DP Solve Optimized (python swaps are expensive)
        if n == 0 or n == 1:
            return 1
        else:
            # Generate dp array and build as you go
            dp = [0] * 2 # Just store the previous two
            dp[0] = 1
            dp[1] = 1
            for i in range(2, n+1):
                temp = dp[0]
                dp[0] = dp[1]
                dp[1] = temp + dp[0]
                
            return dp[-1]