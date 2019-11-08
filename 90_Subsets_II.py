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

# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

# backtrack
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        start = 0
        current = []
        nums.sort()   # unify [2, 1] to [1, 2] to skip duplicate
        self.backtrack(nums, start, current, result)
        return result
    
    def backtrack(self, nums, start, current, result):
        if current not in result:
            result.append(current[:])
        for i in range(start, len(nums)):
            # better way to skip duplicate
            #if i > start and nums[i] == nums[i-1]:
            #    continue
            current.append(nums[i])
            self.backtrack(nums, i+1, current, result)
            current.pop()
        