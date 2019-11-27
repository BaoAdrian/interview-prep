/*
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
*/

class Solution {
    public int climbStairs(int n) {
        // Time: 0ms (100%)
        // Mem: 33.1MB (5.26%)
        if (n == 0 || n == 1) {
            return 1;
        } else {
            int arr[] = new int[3];
            arr[0] = 1;
            arr[1] = 1;
            for (int i = 2; i <= n; i++) {
                int temp = arr[0];
                arr[0] = arr[1];
                arr[1] = temp + arr[0];
            }
            return arr[1];
        }
    }
}