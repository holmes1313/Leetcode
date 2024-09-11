# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:20:52 2020

@author: z.chen7
"""

# 367. Valid Perfect Square

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = num  
        while l <= r:
            mid = (l + r) // 2            
            if mid*mid == num:
                return True
            if mid*mid > num:
                r = mid - 1
            else:
                l = mid + 1
                
        return False

    def isPerfectSquare2(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid**2 == num:
                return True
            elif mid**2 < num < (mid+1)**2:
                return False
            elif mid**2 < num:
                left = mid + 1
            else:
                right = mid - 1