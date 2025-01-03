# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:07:42 2019

@author: z.chen7
"""

# 1137. N-th Tribonacci Number
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537"""

class Solution(object):
    cache = {0: 0, 1: 1, 2: 1}
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.cache:
            self.cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.cache[n]

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n == 2:
            return 1

        else:
            curr = 0
            prev1 = 0
            prev2 = 1
            prev3 = 1
            for i in range(3, n+1):
                curr = prev1 + prev2 + prev3
                prev1 = prev2
                prev2 = prev3
                prev3 = curr

            return curr

        