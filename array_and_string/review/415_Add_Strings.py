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

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1, num2 = num1.zfill(n), num2.zfill(n)

        carry = 0
        ans = []
        for i in range(n-1, -1, -1):
            carry += int(num1[i])
            carry += int(num2[i])

            ans.append(str(carry % 10))
            carry //= 10

        if carry == 1:
            ans.append("1")

        return "".join(ans[::-1])

        


ord("5") - ord("0")
ord('5')
chr(53)
