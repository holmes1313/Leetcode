# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:10:07 2019

@author: z.chen7
"""

# 50. Pow(x, n)

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x ** n
        if n == 0:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        if n < 0:
            self.memo[n] = 1 / self.myPow(x, -n)
            return self.memo[n]
        
        else:
            if n % 2:
                self.memo[n] = x * self.myPow(x, n-1)
            else:
                self.memo[n] = self.myPow(x*x, n // 2)
                
            return self.memo[n]