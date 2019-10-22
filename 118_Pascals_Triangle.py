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
    
    
    