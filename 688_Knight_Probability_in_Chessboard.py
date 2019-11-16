# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:27:15 2019

@author: z.chen7
"""

# 688. Knight Probability in Chessboard
"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and 
attempts to make exactly K moves. The rows and columns are 0 indexed, 
so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. 
Each move is two squares in a cardinal direction, then one square in an orthogonal direction. 

Each time the knight is to move, it chooses one of eight possible moves uniformly 
at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved 
off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""

"""
Approach #1: Dynamic Programming (memo)

Let f[r][c][steps] be the probability of being on square (r, c) after steps steps. 
Based on how a knight moves, we have the following recursion:

Base case:
    if  0 <= r < N and 0 <= c < N:
        f[r][c][0] = 1
    else:
        f[r][c][K] = 0
        
f[r][c][steps]=∑{dr,dc} f[r-dr][c-dc][steps−1] / 8.0

where the sum is taken over the eight (dr, dc)(dr,dc) pairs 
(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2).
"""
import collections

class Solution(object):
    
    def __init__(self):
        self.memo = collections.defaultdict(int)
    
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if r < 0 or r >= N or c < 0 or c >= N:
            return 0
        if K == 0 and 0 <= r < N and 0 <= c < N:
            return 1
        
        steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        
        if (r, c, K) not in self.memo:
            for step in steps:
                self.memo[(r, c, K)] += self.knightProbability(N, K-1, r-step[0], c-step[1]) / 8.0
        return self.memo[(r, c, K)] 


Solution().knightProbability(3, 1, 0, 0)
