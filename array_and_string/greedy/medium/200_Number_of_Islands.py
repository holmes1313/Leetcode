# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:27:54 2019

@author: z.chen7
"""
# 200. Number of Islands
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        num_islands = 0
        # greedy
        # iterate through each element, converting an island to water after we find one
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
            grid[r][c] = "0"

            self.dfs(grid, r+1, c)
            self.dfs(grid, r-1, c)
            self.dfs(grid, r, c+1)
            self.dfs(grid, r, c-1)
