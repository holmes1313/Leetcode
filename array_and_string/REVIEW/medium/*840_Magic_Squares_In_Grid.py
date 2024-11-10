# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:44:04 2019

@author: z.chen7
"""

# 840. Magic Squares In Grid
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagicSquare(x, y):
            # Collect numbers in the 3x3 subgrid
            numbers = [
                grid[x][y], grid[x][y + 1], grid[x][y + 2],
                grid[x + 1][y], grid[x + 1][y + 1], grid[x + 1][y + 2],
                grid[x + 2][y], grid[x + 2][y + 1], grid[x + 2][y + 2]
            ]
            
            # Check if all numbers are distinct and between 1 and 9
            if sorted(numbers) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            # Calculate sums
            row1 = numbers[0] + numbers[1] + numbers[2]
            row2 = numbers[3] + numbers[4] + numbers[5]
            row3 = numbers[6] + numbers[7] + numbers[8]
            col1 = numbers[0] + numbers[3] + numbers[6]
            col2 = numbers[1] + numbers[4] + numbers[7]
            col3 = numbers[2] + numbers[5] + numbers[8]
            diag1 = numbers[0] + numbers[4] + numbers[8]
            diag2 = numbers[2] + numbers[4] + numbers[6]
            
            # Check if all sums are equal to 15
            return (row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15)

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows-2):
            for j in range(cols-2):
                if isMagicSquare(i, j):
                    count += 1

        return count
        