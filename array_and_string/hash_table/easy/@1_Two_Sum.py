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
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}    
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[num] = i
        return False 

# follow up
# what if nums is sorted? - two pointer
# what if nums has dups? - hash map