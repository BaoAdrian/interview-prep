/*
 * Min Path Sum (#64)
 * https://leetcode.com/problems/minimum-path-sum/
 * 

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes 
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 */


class Solution {
    public int minPathSum(int[][] grid) {
        // Time: 2ms: (24%)
        // Mem: 42.7MB (68.92%)

        if (grid == null || grid.length == 0) {
            return 0;   
        }
        
        int[][] dp = new int[grid.length][grid[0].length];
        
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp[0].length; j++) {
                dp[i][j] += grid[i][j];
                if (i > 0 && j > 0) { // Came from either top or left
                    dp[i][j] += Math.min(dp[i - 1][j], dp[i][j - 1]);
                } else if (i > 0) { // Came from top
                    dp[i][j] += dp[i - 1][j];
                } else if (j > 0) { // Came from left
                    dp[i][j] += dp[i][j - 1];
                }
            }
        }

        // Last corner will contain the minimum path sum
        return dp[dp.length-1][dp[0].length - 1];
    }
}