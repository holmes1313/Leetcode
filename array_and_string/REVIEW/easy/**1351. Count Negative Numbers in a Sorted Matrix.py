"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

"""
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # Start from the top-right corner
        i = 0
        j = cols - 1
        count = 0

        while i < rows and j >= 0:
            if grid[i][j] < 0:
                # Count all remaining rows in this column
                count += (rows - i)
                # Move left
                j -= 1
            else:
                # Move down
                i += 1
        
        return count