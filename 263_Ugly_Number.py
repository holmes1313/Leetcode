# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:21:31 2019

@author: z.chen7
"""

# 263. Ugly Number
"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for f in [2, 3, 5]:
            while num % f == 0:
                num /= f
                
        return num == 1
        