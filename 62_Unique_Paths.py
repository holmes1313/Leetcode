# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:50:54 2019

@author: z.chen7
"""

# 62. Unique Paths

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is 
trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

"""
Since the robot can only move right and down, when it arrives at a point, 
it either arrives from left or above. If we use dp[i][j] for the number of 
unique paths to arrive at the point (i, j), then the state equation is dp[i][j] = dp[i][j - 1] + dp[i - 1][j]. 
Moreover, we have the base cases dp[0][j] = dp[i][0] = 1 for all valid i and j.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        
        dp = [[1 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
        return dp[m][n]
        


class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        
        if m == 1 or n == 1:
            return 1
        
        if (m, n) not in self.memo:
            self.memo[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        print self.memo
        return self.memo[(m, n)]











