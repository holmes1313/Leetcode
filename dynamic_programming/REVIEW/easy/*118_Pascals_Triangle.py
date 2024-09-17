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
"""# -*- coding: utf-8 -*-
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
from typing import List


# matrix -> coordinates
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1] * (i+1) for i in range(numRows)]
        
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result

    def generate2(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        triangle =  [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1 for _ in range(i+1)]
            for k in range(1, len(row)-1):
                row[k] = triangle[i-1][k-1] + triangle[i-1][k]
            triangle.append(row)
        return triangle


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
        