# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:42:40 2019

@author: z.chen7
"""

# 7. Reverse Integer
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            symbol = -1
            str_x = str(x)[1:]
        else:
            symbol = 1
            str_x = str(x)
        
        result = int(str_x[::-1]) * symbol
        
        mina = -2 ** 31
        maxa = 2**31 -1
        # # handle 32 bit overflow
        if mina<= result <= maxa:  
            return result  
        else:  
            return 0
