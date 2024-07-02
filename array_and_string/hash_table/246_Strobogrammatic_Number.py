# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:17:56 2019

@author: z.chen7
"""

# 246. Strobogrammatic Number

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        l = 0
        r = len(num) - 1
        
        while l <= r:
            if num[l] not in dic or dic[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
            
        return True
            
        