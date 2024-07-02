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
        if not nums or len(nums) < 4:
            return None
        
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.threeSum(nums, i, target, result)
            
        return result
        
    def threeSum(self, nums, index, target, result):
        head = nums[index]
        for i in range(index+1, len(nums) - 2):
            if i > index+1 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                s = head + nums[i] + nums[left] + nums[right]
            
                if s == target:
                    result.append([head, nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1    
                elif s > target:
                    right -= 1
                elif s < target:
                    left += 1


from typing import List


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        for first_index in range(len(nums)):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue

            for second_index in range(first_index + 1, len(nums)):
                if second_index > first_index + 1 and nums[second_index] == nums[second_index - 1]:
                    continue

                left = second_index + 1
                right = len(nums) - 1
                while left < right:
                    sum4 = nums[first_index] + nums[second_index] + nums[left] + nums[right]
                    if sum4 == target:
                        output.append([nums[first_index], nums[second_index], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif sum4 < target:
                        left += 1
                    else:
                        right -= 1

        return output