# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:01:34 2019

@author: z.chen7
"""

# 46. Permutations
"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        nums.sort()
        self.dfs(nums, result, current)
        return result
    
    
    def dfs(self, nums, result, current):
        if len(current) == len(nums):
            result.append(current[:])
            
        else:
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                self.dfs(nums, result, current)
                current.pop()
        