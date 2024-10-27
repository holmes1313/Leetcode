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
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        result = []
        backtrack([])
        return result


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                used[i] = False
                path.pop()

        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result
        
    def permute(self, nums):
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
