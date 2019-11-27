"""
Word Search I
https://leetcode.com/problems/word-search/


Given a 2D board and a word, find if the word 
exists in the grid.

The word can be constructed from letters of 
sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time: 340ms (79.23%)
        Mem: 13.7MB (100%)
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        
        return False
    
    def dfs(self, board, i, j, count, word):
        # Found it
        if count == len(word):
            return True
        
        # Bounds
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]:
            return False
        
        # Store temp and replace with empty string for dfs
        temp = board[i][j]
        board[i][j] = " "
        
        # Traverse the 4 corners
        count += 1
        found = self.dfs(board, i + 1, j, count, word) or self.dfs(board, i - 1, j, count, word) or self.dfs(board, i, j + 1, count, word) or self.dfs(board, i, j - 1, count, word)
        board[i][j] = temp # restore back
        return found
        
            