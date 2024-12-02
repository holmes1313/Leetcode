# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:37:23 2019

@author: z.chen7
"""

# 77. Combinations
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result
