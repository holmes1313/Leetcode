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
        nums = [i for i in range(1, n+1)]
        current = []
        result = []
        start = 0
        self.backtrack(nums, k, start, current, result)
        return result
        
        
    def backtrack(self, nums, k, start, current, result):
        if len(current) == k:
            result.append(current[:])
            
        else:
            for i in range(start, len(nums)):
                current.append(nums[i])
                self.backtrack(nums, k, i+1, current, result)
                current.pop()
        