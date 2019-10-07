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

def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num1 = list(num1)
    num2 = list(num2)
    carry = 0
    result = []
    
    while num1 or num2:
        n1 = ord(num1.pop()) - ord("0") if num1 else 0
        n2 = ord(num2.pop()) - ord("0") if num2 else 0
        
        s = n1 + n2 + carry
        result.append(s % 10)
        carry = s // 10
        
    if carry:
        result.append(carry)
        
    return "".join([str(n) for n in result][::-1])



ord("5") - ord("0")
