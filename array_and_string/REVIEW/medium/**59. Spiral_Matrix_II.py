# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:41:12 2019

@author: z.chen7
"""

# 59. Spiral Matrix II

"""
Given a positive integer n, generate a square matrix filled with elements 
from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]

        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # direction 
        direction_idx = 0
        # boundaries
        top = 0
        bottom = n - 1
        right = n - 1
        left = 0
        # start number
        num = 1
        # start spot
        x, y = 0, 0

        while num <= n * n:
            matrix[x][y] = num
            num += 1

            # next spot
            dx, dy = directions[direction_idx]
            nx, ny = x + dx, y + dy

            # check if we need to change direction
            if not (top <= nx <= bottom and left <= ny <= right):
                if direction_idx == 0:
                    top += 1
                elif direction_idx == 1:
                    right -= 1
                elif direction_idx == 2:
                    bottom -= 1
                elif direction_idx == 3:
                    left += 1

                direction_idx = (direction_idx + 1) % 4
                dx, dy = directions[direction_idx]
                nx, ny = x + dx, y + dy

            x, y = nx, ny

        return matrix
        

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix
