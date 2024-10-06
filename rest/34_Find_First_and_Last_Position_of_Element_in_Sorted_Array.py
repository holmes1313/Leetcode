# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:34:08 2019

@author: z.chen7
"""

# 34. Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lowerBound = self.lower_bound(nums, target)
        # upperBound = self.upper_bound(nums, target)
        upperBound = self.lower_bound(nums, target+1) - 1
        return [lowerBound, upperBound] if upperBound >= lowerBound else [-1, -1]
        
    def lower_bound(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L += 1
            else:
                R -= 1
        return L
    
    def upper_bound(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] > target:
                R -= 1
            else:
                L += 1
        return R
        