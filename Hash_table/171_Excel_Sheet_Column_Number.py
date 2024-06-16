# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:47:33 2019

@author: z.chen7
"""
# 171. Excel Sheet Column Number

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None
        
        result = 0
        for i, l in enumerate(list(s[::-1])):
            value = ord(l) - ord('A') + 1
            result += (26 ** i) * value
        return result
        