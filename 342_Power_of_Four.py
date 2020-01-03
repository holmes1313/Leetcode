# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:03:05 2020

@author: z.chen7
"""

# 342. Power of Four

"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        while num % 4 == 0:
            num /= 4
            
        return num == 1
        