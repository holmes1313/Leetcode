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
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # Decimal 65 in ASCII corresponds to char 'A'
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}

        result = 0
        factor = 0
        for digit in columnTitle[::-1]:
            result += alpha_map[digit] * (26 ** factor)
            factor += 1

        return result


        