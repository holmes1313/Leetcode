# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:55:11 2019

@author: z.chen7
"""
# 994. Rotting Oranges
"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""


# simple bfs solution use all rotten orange as start position
# use count_one to count the number of 1, when one fresh orange become rotten orange, count_one -= 1 
# once bfs over, the count_one should be 0.


import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rn, cn = len(grid), len(grid[0])
        count_one = 0
        queue = collections.deque()
        minite = 0
        
        for i in range(rn):
            for j in range(cn):
                if grid[i][j] == 1:
                    count_one += 1
                elif grid[i][j] == 2:
                    queue.appendleft((i, j))   # add all rotting oranges into the queue
        
        while queue and count_one:  # queue represents newly rotting oranges and we continue if there's fresh one left
            for _ in range(len(queue)):   # for each batch(minute)
                x, y = queue.pop()
                for x, y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if (0 <= x < rn) and (0 <= y < cn):
                        if grid[x][y] == 1:
                            grid[x][y] == 2
                            count_one -= 1
                            queue.appendleft([x, y])
            minite += 1
        
        if count_one:
            return -1
        else:
            return minite
                            
                        
                    
                
                
                
           
                
                
            