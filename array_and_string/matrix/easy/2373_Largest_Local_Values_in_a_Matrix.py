"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

 

Example 1:


Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:


Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
"""
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(grid)
        #result = [[0 for i in range(len(grid) - 2)] for i in range(len(grid) - 2)]
        result = [[0] * (N-2) for _ in range(N-2)]
        for i in range(N - 2):
            for j in range(N - 2):
                max_local = 0
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        max_local = max(max_local, grid[x][y])
                result[i][j] = max_local

        return result