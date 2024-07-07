# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:30:44 2019

@author: z.chen7
"""

# 867. Transpose Matrix
"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #return [[row[i] for row in A] for i in range(len(A[0]))]
        return list(zip(*A))


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [[0] * rows for _ in range(cols)]
        for row in range(len(ans)):
            for col in range(len(ans[0])):
                ans[row][col] = matrix[col][row]

        return ans