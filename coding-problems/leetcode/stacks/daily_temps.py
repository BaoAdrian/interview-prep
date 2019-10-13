"""
Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each 
day in the input, tells you how many days you would have to wait until a 
warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range 
[1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res
        
    
    def dailyTemperaturesBrute(self, T):
        output = []
        
        for i in range(len(T)):
            runner = 0
            for j in range(i, len(T), 1):
                if T[i] >= T[j]:
                    runner += 1
                else:
                    break
                if j+1 == len(T):
                    runner = 0
            output.append(runner)
        return output