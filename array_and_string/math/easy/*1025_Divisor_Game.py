# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:43:56 2019

@author: z.chen7
"""

# 1025. Divisor Game
"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000
"""
class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
    
        # Base case: If n = 1, Alice loses
        dp[1] = False
        
        # Fill the DP table
        for i in range(2, n + 1):
            # Check all possible moves
            for x in range(1, i):
                if i % x == 0:
                    if not dp[i - x]:
                        dp[i] = True
                        break
        
        return dp[n]


class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Alice wins if n is even
        return n % 2 == 0