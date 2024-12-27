"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        rot_queue = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rot_queue.append((i, j))

        min_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while rot_queue and fresh_count > 0:
            min_passed += 1
            for _ in range(len(rot_queue)):
                i, j = rot_queue.popleft()
                for x, y in directions:
                    i_new = i + x
                    j_new = j + y
                    if 0 <= i_new < rows and 0 <= j_new < cols and grid[i_new][j_new] == 1:
                        grid[i_new][j_new] = 2
                        fresh_count -= 1
                        rot_queue.append((i_new, j_new))

        if fresh_count == 0:
            return min_passed
        else:
            return -1


