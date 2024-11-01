# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:10:26 2019

@author: z.chen7
"""

# 415. Add Strings
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly."""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return "".join(result[::-1])
        