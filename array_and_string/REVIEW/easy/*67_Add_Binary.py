# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:18:10 2019

@author: z.chen7
"""

# 67. Add Binary
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

# bit manipulation
# binary -> decimal
# eval('0b' + '11')
# decimal -> binary
# bin(100)[2:]

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return "{0:b}".format(int(a, 2) + int(b, 2))
        
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0

            total = d1 + d2 + carry
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1

        return ''.join(result[::-1])
