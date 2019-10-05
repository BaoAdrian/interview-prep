"""
Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin/submissions/

There is a robot starting at position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after 
it completes its moves.

The move sequence is represented by a string, and the character moves[i] 
represents its ith move. Valid moves are R (right), L (left), U (up), and
 D (down). If the robot returns to the origin after it finishes all of its
  moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always
 make the robot move to the right once, "L" will always make it move left,
  etc. Also, assume that the magnitude of the robot's movement is the same 
  for each move.

Example 1:

Input: "UD"
Output: true 
Explanation: The robot moves up once, and then down once. All moves have 
the same magnitude, so it ended up at the origin where it started. 
Therefore, we return true.
 

Example 2:

Input: "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left 
of the origin. We return false because it is not at the origin at the end 
of its moves.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Time:   60ms (67%)
        Memory: 14MB (6.9%)
        """
        x, y = 0, 0
        for move in moves:
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
        
        return x == 0 and y == 0
    
    def judgeCircdle(self, moves: str) -> bool:
        """
        Time:   40ms   (91.83%)
        Memory: 14.1mB (6.90%)
        """
        # Each moves requires its counter to match
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')