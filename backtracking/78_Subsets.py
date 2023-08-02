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

# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

class Solution(object):
    def subsets(self, nums):
        result = []
        start = 0
        current = []
        self.backtrack(nums, start, current, result)
        return result
    
    def backtrack(self, nums, start, current, result):
        result.append(current[:])    # make copy of current
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.backtrack(nums, i+1, current, result)   # i + 1 instead of start + 1
            current.pop()


from typing import List


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtracking(curr, start):
            result.append(curr[:])

            for i in range(start, len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtracking(curr, i + 1)
                    curr.pop()

        result = []
        backtracking([], 0)
        return result
