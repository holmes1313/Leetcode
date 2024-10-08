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
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        distance = ord("A")
        while n > 0:
            n -= 1
            digit = n % 26
            digit = chr(digit + distance)
            result = digit + result
            n = n // 26
        return result
    
    def convertToNum(self, col):
        digit = 0
        result = 0
        for c in col[::-1]:
            result += (26 ** digit) * (ord(c) - ord('A') + 1)
            digit += 1
        return result


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            ans += chr(ord("A") + offset)
            columnNumber = (columnNumber - 1) // 26
        return ans[::-1]
        