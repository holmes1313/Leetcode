# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:52:29 2019

@author: z.chen7
"""

# 74. Search a 2D Matrix
"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n-1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid//n][mid%n]
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return True


        return False
