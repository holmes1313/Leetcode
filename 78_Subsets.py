# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:04:04 2019

@author: z.chen7
"""

# 78. Subsets

"""

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
            
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        self.dfs(result, temp, nums, 0)
        return result
        
    def dfs(self, result, path, nums, start):
        result.append(path)
        for i in range(start, len(nums)):
            self.dfs(result, nums, start+1, path + [nums[i]])