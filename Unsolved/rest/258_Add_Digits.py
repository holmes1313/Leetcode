# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:14:26 2019

@author: z.chen7
"""

# 258. Add Digits
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""

class Solution(object):
    # recursively
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 <= num <= 9:
            return num
        
        tmp = 0
        while num:
            tmp += num % 10
            num //= 10
        
    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum(map(int,list(str(num))))
        return num
        return self.addDigits(tmp)