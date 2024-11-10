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

        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1

        counter = collections.Counter(nums)
        result = []
        backtrack([], counter)
        return result