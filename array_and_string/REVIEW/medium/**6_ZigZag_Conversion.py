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
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        going_down = True  # direction flag

        for cha in s:
            rows[curr_row] += cha

            if curr_row == 0:
                going_down = True
            elif curr_row == numRows - 1:
                going_down = False

            curr_row += 1 if going_down else -1

        return "".join(rows)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row_idx = 0
        diff = 1
        for cha in s:
            rows[row_idx] += cha

            if row_idx == numRows - 1:
                diff = -1
            elif row_idx == 0:
                diff = 1

            row_idx += diff
        
        return "".join(rows)
