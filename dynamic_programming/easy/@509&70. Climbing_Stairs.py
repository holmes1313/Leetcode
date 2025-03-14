# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:41:15 2019

@author: z.chen7
"""

# 70. Climbing Stairs

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def helper(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            if n in memo:
                return memo[n]

            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

        return helper(n)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        first, second = 1, 2

        for i in range(3, n+1):
            curr = first + second
            first = second
            second = curr

        return second
