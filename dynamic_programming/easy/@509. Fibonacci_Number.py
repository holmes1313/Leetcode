# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:21:46 2019

@author: z.chen7
"""

# 509. Fibonacci Number
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30."""

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n==0:
                return 0

            if n==1:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        memo = {}
        return helper(n)

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        prev1 = 0
        prev2 = 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return curr
