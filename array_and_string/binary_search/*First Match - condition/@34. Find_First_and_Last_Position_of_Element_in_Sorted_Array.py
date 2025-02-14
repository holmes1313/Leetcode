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
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left - 1

        start = find_first(nums, target)
        end = find_last(nums, target)

        if start <= end:
            return [start, end]
        else:
            return [-1, -1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left < right:
            return [left, right-1]
        else:
            return [-1, -1]
