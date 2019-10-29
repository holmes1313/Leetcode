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



