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

class Solution_200(object):
    def numIslands(self, matrix):
        if not matrix:
            return 0
        rn = len(matrix)
        cn = len(matrix[0])
        num = 0
        for i in range(rn):
            for j in range(cn):
                if matrix[i][j] == '1':
                    num += 1
                    self.bfs(matrix, i, j, rn, cn)
        #print matrix
        return num    
    def bfs(self, matrix, i, j, rn, cn):
        queue = collections.deque()
        queue.appendleft((i, j))
        while queue:
            x, y = queue.pop()
            # checking current element
            if matrix[x][y] == '1':
                matrix[x][y] = '2'
                # appending other elements
                for m, n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= m < rn and 0 <= n < cn and matrix[m][n] == '1':
                        queue.appendleft((m, n))


input = [['1', '1', '0'],
         ['0', '0', '1']]

Solution().numIslands(input)
