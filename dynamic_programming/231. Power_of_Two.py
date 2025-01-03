# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:19:59 2019

@author: z.chen7
"""

# 231. Power of Two

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n /= 2
        
        return n == 1
        