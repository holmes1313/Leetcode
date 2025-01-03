# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:17:35 2019

@author: z.chen7
"""

# 172. Factorial Trailing Zeroes

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

"""
Since 0 only company with 5*2
So only need to count the volume of 5 factor. (because 2 always enough)

So..
100! 's zero has => floor(100/5) + floor(100/25) = floor(100/5) + floor((100/5)/5)
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            n //= 5
            count += n

        return count

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_factorial = 1
        for i in range(1, n+1):
            n_factorial *= i

        zero_count = 0
        while n_factorial % 10 == 0:
            n_factorial //= 10
            zero_count += 1

        return zero_count


