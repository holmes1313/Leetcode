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
def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x >= 0:
        a = int(str(x)[::-1])
    else:
        a = -1 * int(str(x)[1:][::-1])
    
    mina = -2 ** 31
    maxa = 2**31 -1
    # # handle 32 bit overflow
    if mina<= a <= maxa:  
        return a  
    else:  
        return 0


reverse(120)
reverse(-123)

1534236469 >= 0