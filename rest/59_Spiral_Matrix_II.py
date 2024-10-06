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
        if not n:
            return []
        
        result = [[0] * n for _ in range(n)]
        left = 0
        right = n-1
        top = 0
        down = n-1
        num = 1
        
        while left <= right and top <= down:
            # from left to right
            for i in range(left, right+1):
                result[top][i] = num
                num += 1
            top += 1
            
            # from top to down
            for i in range(top, down+1):
                result[i][right] = num
                num += 1
            right -= 1
            
            # from right to left
            for i in range(right, left-1, -1):
                result[down][i] = num
                num += 1
            down -= 1
            
            # from down to top
            for i in range(down, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
            
        return result
            
