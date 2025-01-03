# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:19:22 2019

@author: z.chen7
"""

# 18. 4Sum

"""
Given an array nums of n integers and an integer target, are there elements 
a, b, c, and d in nums such that a + b + c + d = target? Find all 
unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                left = j+1
                right = n-1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1

                        left += 1
                        right -= 1

        return result