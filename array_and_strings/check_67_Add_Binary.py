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

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return bin(eval('0b'+a) + eval('0b'+b))[2:]

eval('0b11')
bin(3)


# add two binary from back to front, when 1+1 we need a carry.
def addBinary_2(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    
    if (a[-1] == '0') and (b[-1] == '0'):
        return addBinary_2(a[:-1], b[:-1]) + '0'
    
    elif (a[-1] == '1') and (b[-1] == '1'):
        return addBinary_2(addBinary_2(a[:-1], b[:-1]), '1') + '0'
    
    else:
        return addBinary_2(a[:-1], b[:-1]) + '1'
    

addBinary_2('1', '10')


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n = max(len(a), len(b))
        if len(a) < n:
            for _ in range(n - len(a)):
                a = "0" + a

        if len(b) < n:
            for _ in range(n - len(b)):
                b = "0" + b

        carry = 0
        ans = ""
        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1

            if b[i] == "1":
                carry += 1
            # remainder
            ans = str(carry % 2) + ans
            # quotient
            carry //= 2

        if carry == 1:
            ans = "1" + ans

        return ans