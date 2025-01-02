# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:02:06 2019

@author: z.chen7
"""

# 118. Pascal's Triangle
# ***
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            row = [1] * (i+1)
            if i >= 2:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle


    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1] * (i+1)for i in range(numRows)]

        if numRows > 2:
            for i in range(2, numRows):
                last_row = triangle[i-1]
                row = triangle[i]
                for j in range(1, len(row)-1):
                    row[j] = last_row[j-1] + last_row[j]

        return  triangle
        