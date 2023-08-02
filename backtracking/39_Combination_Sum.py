# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:07:30 2019

@author: z.chen7
"""

# 39. Combination Sum
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# backtrack
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []
        start = 0
        self.backtrack(candidates, start, current, result, target)
        return result
    
    def backtrack(self, nums, start, current, result, target):
        
        if sum(current) == target:
            result.append(current[:])
            
        elif sum(current) > target:
            return
        
        else:
            for i in range(start, len(nums)):
                current.append(nums[i])
                self.backtrack(nums, i, current, result, target)  # not i + 1 because we can reuse same elements
                current.pop()


from typing import List


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtracking(curr, start):
            if sum(curr) == target:
                # make a deep copy of the current combination
                result.append(curr[:])
                return

            if sum(curr) > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtracking(curr, i)
                curr.pop()

        result = []
        backtracking([], 0)
        return result

