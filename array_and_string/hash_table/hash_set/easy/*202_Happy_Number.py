# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:23:03 2019

@author: z.chen7
"""

# 202. Happy Number
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares 
of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# 2 screnarios
# It eventually gets to 111.
# It eventually gets stuck in a cycle.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(d)**2 for d in str(n)])
        return n == 1

