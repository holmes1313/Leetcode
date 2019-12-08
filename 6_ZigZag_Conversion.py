# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:48:44 2019

@author: z.chen7
"""

# 6. ZigZag Conversion

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        
        rows = [''] * numRows
        rowIndex = 0
        step = 1
        
        for char in s:
            rows[rowIndex] += char
            
            if rowIndex == 0:
                step = 1
                
            elif rowIndex == numRows - 1:
                step = -1
                
            rowIndex += step
            
        return ''.join(rows)