# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:34:58 2019

@author: z.chen7
"""

# 43. Multiply Strings

"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for i, d1 in enumerate(num1[::-1]):
            tmp = int(d1) * 10**i
            for j, d2 in enumerate(num2[::-1]):
                result += tmp * (int(d2) * 10**j)
                
        return str(result)
                

