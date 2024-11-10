"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

 

Example 1:


Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
Example 2:


Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        shapes = set()

        def dfs(i, j, origin_i, origin_j):
            shape = []
            stack = [(i, j)]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while stack:
                i, j = stack.pop()
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                    grid[i][j] = 0
                    # Record the relative position
                    shape.append((origin_i - i, origin_j - j))
                    for x, y in directions:
                        stack.append((i+x, j+y))

            return tuple(shape)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = dfs(i, j, i, j)
                    shapes.add(tuple(shape)) # Add the shape to the set as a tuple

        return len(shapes)

        