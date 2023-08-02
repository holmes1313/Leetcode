# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:00:23 2019

@author: z.chen7
"""

# 47. Permutations II
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
import collections

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        # use counter to mark if a duplicate has been used
        counter = collections.Counter(nums)
        self.backtrack(nums, result, current, counter)
        return result
    
    def backtrack(self, nums, result, current, counter):
        if len(current) == len(nums):
            result.append(current[:])        
        else:
            for x in counter:
                if counter[x] > 0:
                    current.append(x)
                    counter[x] -= 1
                    self.backtrack(nums, result, current, counter)
                    counter[x] += 1
                    current.pop()
        
        