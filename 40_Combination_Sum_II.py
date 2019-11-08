# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:41:32 2019

@author: z.chen7
"""

# 40. Combination Sum II
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []
        start = 0
        candidates.sort()
        self.backtrack(candidates, start, current, result, target)
        return result
    
    def backtrack(self, nums, start, current, result, target):
        if sum(current) > target:
            return
        elif sum(current) == target: #and current not in result:
            result.append(current[:])
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                self.backtrack(nums, i+1, current, result, target)
                current.pop()
        