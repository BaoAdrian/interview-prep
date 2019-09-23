# LeetCode
- [Univalued Binary Tree](#univalued-binary-tree)
- [Valid Parentheses](#valid-parentheses)
- [Max Subarrays](#max-subarrays)


# Univalued Binary Tree
Problem: https://leetcode.com/problems/univalued-binary-tree/ 

Description: \
A binary tree is univalued if every node in the tree has the same value. \
Return `true` if and only if the given tree is univalued.

Examples:

<img src="./images/unival-example1.png" alt="drawing" width="250"/>

```
Input: [1,1,1,1,1,null,1]
Output: true
```

<img src="./images/unival-example2.png" alt="drawing" width="250"/>

```
Input: [2,2,2,5,2]
Output: false
```

# Valid Parentheses
Problem: https://leetcode.com/problems/valid-parentheses/

Description: \
Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
    > Open brackets must be closed by the same type of brackets.
    > Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Examples:

```
Input: "()"
Output: true
```

```
Input: "[{({[[[()]]]})}]"
Output: true
```

```
Input: "([)]"
Output: false
```

# Max Subarrays
Problem: https://leetcode.com/problems/maximum-subarray/
Description: \
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example: \

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
