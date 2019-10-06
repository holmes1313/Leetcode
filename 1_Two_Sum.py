# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:39:54 2019

@author: z.chen7
"""

# 1. Two Sum
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def twoSum(nums, target):
    """
    :type nums: List[int], e.g. [2, 7, 11, 15]
    :type target: int, e.g. 9
    :rtype: List[int], e.g. [0, 1]
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[i] == target:
                return [i, j]

def twoSum_2(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        else:
            seen[num] = index

twoSum_2([2, 7, 11, 15], 9)
