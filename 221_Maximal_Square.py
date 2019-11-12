# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:14:43 2019

@author: z.chen7
"""

# 221. Maximal Square
"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

"""
When i > 0 and j > 0, 
if matrix[i][j] = '0', then dp[i][j] = 0 since no square will be able to contain the '0' at that cell. 
If matrix[i][j] = '1', we will have dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1, 
which means that the square will be limited by its left, upper and upper-left neighbors.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        dp = [[1 if char == '1' else 0 for char in row] for row in matrix]
        max_len = dp[0][0]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i != 0 and j != 0 and dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_len = max(max_len, dp[i][j])
                
        return max_len * max_len