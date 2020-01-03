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

# to get value of "5" without converting it to int
# ord("5") - ord("0")

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1) + int(num2))
        
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        result = ''
        while num1 or num2 or carry:
            n1 = ord(num1.pop()) - ord('0') if num1 else 0
            n2 = ord(num2.pop()) - ord('0') if num2 else 0
            
            s = n1 + n2 + carry
            
            result = str(s % 10) + result
            carry = s // 10
            
        return result
            


ord("5") - ord("0")
ord('5')
chr(53)
