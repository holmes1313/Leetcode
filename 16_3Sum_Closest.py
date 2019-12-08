# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:31:04 2019

@author: z.chen7
"""

# 16. 3Sum Closest
"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return None
        
        result = sum(nums[:3])
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(result - target):
                    result = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return result
        