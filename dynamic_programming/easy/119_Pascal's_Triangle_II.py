# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:30:43 2019

@author: z.chen7
"""

# 119. Pascal's Triangle II
"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        for i in range(rowIndex+1):
            row = [1] * (i+1)

            if i > 1:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle[rowIndex] 
        
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            row = [1]

        elif rowIndex == 1:
            row = [1, 1]

        elif rowIndex > 1:
            row = [1, 1]
            for i in range(2, rowIndex+1):
                new_row = [1] * (i + 1)
                for j in range(1, i):
                    new_row[j] = row[j-1] + row[j]
                row = new_row
        return row
        