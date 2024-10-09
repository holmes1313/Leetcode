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
        count = 0
        for row in grid:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            # left is first negative
            # right is last positive
            count += len(row) - left
        return count

    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(grid[0])
        lastPositiveIdx = n - 1

        for row in grid:
            while lastPositiveIdx >= 0 and row[lastPositiveIdx] < 0:
                lastPositiveIdx -= 1
            count += n - (lastPositiveIdx + 1)

        return count