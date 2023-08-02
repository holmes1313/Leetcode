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
        self.backtrack(nums, current, result)
        return result
    
    def backtrack(self, nums, current, result):
        if len(current) == len(nums):
            result.append(current[:])
        else:
            for n in nums:
                if n not in current:  # new element
                    current.append(n)
                    self.backtrack(nums, current, result)
                    current.pop()
                  
# use Counter
import collections

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        current = []
        result = []
        count = collections.Counter(nums)
        self.backtrack(nums, count, current, result)
        return result
    
    def backtrack(self, nums, count, current, result):
        if len(current) == len(nums):
            result.append(current[:])
        else:
            for n in count:
                if count[n]:
                    current.append(n)
                    count[n] -= 1
                    self.backtrack(nums, count, current, result)
                    current.pop()
                    count[n] += 1