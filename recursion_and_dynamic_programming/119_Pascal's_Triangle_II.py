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
from typing import List


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        return [1] + self.helper(self.getRow(rowIndex - 1)) + [1]
        
    
    def helper(self, level):
        result = []
        for i in range(len(level) - 1):
            result.append(level[i] + level[i+1])
        return result

    def getRow2(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        prev = self.getRow(rowIndex - 1)
        curr = [1 for _ in range(rowIndex+1)]
        for i in range(len(prev)-1):
            curr[i+1] = prev[i] + prev[i+1]

        return curr

        