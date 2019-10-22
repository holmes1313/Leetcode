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

import collections

class Solution(object):
    
    def numIslands(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        count = 0
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                
                if matrix[i][j] == '1':
                    count += 1
                    # breath first search
                    self.findPartOfIsland(matrix, i, j, r, c)
                    
        return count
                    
                    
    def findPartOfIsland(self, matrix, i, j, r, c):
        
        queue = collections.deque()
        queue.appendleft((i, j))
        
        while queue:
            loc = queue.pop()
            x = loc[0]
            y = loc[1]
            if matrix[x][y] == '1':
                matrix[x][y] = '2'
                self.appendToQueue(queue, x-1, y, r, c)
                self.appendToQueue(queue, x+1, y, r, c)
                self.appendToQueue(queue, x, y-1, r, c)
                self.appendToQueue(queue, x, y+1, r, c)
    
    def appendToQueue(self, queue, x, y, r, c):
        if (x >= 0) and (x < r) and (y >= 0) and (y < c):
            queue.appendleft((x, y))
        


input = [['1', '1', '0'],
         ['0', '0', '1']]

Solution().numIslands(input)
