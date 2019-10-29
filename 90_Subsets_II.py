# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:15:57 2019

@author: z.chen7
"""

# 90. Subsets II

"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# backtracking

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result
        
        
    def dfs(self, nums, index, current, result):
        result.append(current[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.dfs(nums, i+1, current, result)
            current.pop()