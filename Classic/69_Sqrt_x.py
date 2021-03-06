# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:43:20 2019

@author: z.chen7
"""

# 69. Sqrt(x)
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

# binary search

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        
        while l <= r:
            
            mid = (l+r) // 2
            
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            
            elif x < mid*mid :
                r = mid - 1
            
            else:
                l = mid + 1
