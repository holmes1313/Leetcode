# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:37:38 2019

@author: z.chen7
"""

# 168. Excel Sheet Column Title
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

# https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []

        while columnNumber > 0:
            columnNumber -= 1   # adjust for 0-based index
            remainder = columnNumber % 26
            result.append(chr(ord('A')+remainder))
            columnNumber //= 26    #move to the next "digit"

        return "".join(result[::-1])
