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

class Solution:
    def addBinary2(self, a: str, b: str) -> str:
        # int(a, 2) is used to convert a binary string (represented by a) into its decimal (base-10) integer equivalent.
        # {0:b} tells Python to take the first argument of format(), convert it to binary, and then substitute that into the string.
        return "{0:b}".format(int(a, 2) + int(b, 2))

    # Bit-by-Bit Computation
    def addBinary(self, a: str, b: str) -> str:
        # zfill() method is used to pad a string with zeros on the left, ensuring that the string reaches a specified length. 
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1

            if b[i] == "1":
                carry += 1

            answer.append(str(carry % 2))
            carry //= 2

        if carry == 1:
            answer.append("1")

        return "".join(answer[::-1])