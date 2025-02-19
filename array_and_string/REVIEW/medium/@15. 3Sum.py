# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:27:33 2019

@author: z.chen7
"""
# 15. 3Sum
"""
Given an array nums of n integers, are there elements a, b, c in nums such 
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()
            for j in range(i+1, n):
                if j > i and nums[j] == nums[j-1]:
                    continue

                if 0 - nums[i] - nums[j] in seen:
                    output.append([nums[i], 0 - nums[i] - nums[j], nums[j]])

                seen.add(nums[j])

        return output
