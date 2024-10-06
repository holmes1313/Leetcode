# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:17:59 2019

@author: z.chen7
"""
# 54. Spiral Matrix
"""
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


# recursion
# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
"""
use list(zip(*matrix))[::-1] to convert
[[4, 5, 6],
 [7, 8, 9]]
to 
[[6, 9],
 [5, 8],
 [4, 7]]
"""
def spiralOrder(matrix):
    if not matrix:
        return []
    
    head = matrix.pop(0)
    if len(matrix) > 1:
        rest = spiralOrder(list(zip(*matrix))[::-1])
    elif len(matrix) == 1:
        rest = list(matrix[0][::-1])
    # when matrix [[1]]
    else:
        rest = []
    return list(head) + rest


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
spiralOrder(matrix)




input = [[4, 5, 6],
         [7, 8, 9]]

list(zip(input))
list(zip(input[0], input[1]))
list(zip(*input))



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1
        result = []
        
        while left <= right and top <= down:
            # left to right
            result.extend(matrix[top][left: right+1])
            top += 1
            
            # top to down
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right -= 1
            
            # right to left
            if top <= down:
                result.extend(matrix[down][left: right+1][::-1])  # reverse a part of a list
                down -= 1
            
            # down to top
            if left <= right:
                for i in range(down, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result

            
# reverse a part of a list
# list[a:b+1][::-1]
# list[b:a-1][::-1] might go wrong as list[-1] refers to list[len(list) - 1]
# reverse index
# range(b, a-1, -1)