# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:36:43 2019

@author: z.chen7
"""

# 63. Unique Paths II
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""

"""
Due to obstacles, some boundary points are no longer reachable and need to be 
initialized to 0. For example, if obstacleGrid is like [0, 0, 1, 0, 0], 
then the last three points are not reachable and need to be initialized to be 0. 
The result is [1, 1, 0, 0, 0].
"""
# list comprehension [f(x) if condition else g(x) for x in sequence]

class Solution(object):
    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rnum = len(obstacleGrid)
        cnum = len(obstacleGrid[0])
        # build dp matrix (rnum+1) * (cnum+1)
        dp = [[0 for c in range(cnum+1)] for r in range(rnum+1)]
        dp[0][1] = 1
        for i in range(1, rnum+1):
            for j in range(1, cnum+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rnum][cnum]