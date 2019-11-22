# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:23:34 2019

@author: z.chen7
"""

# 283. Move Zeroes
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations."""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        
        """
        if not nums:
            return None
        
        nonZeroIndex = 0
        for n in nums:
            if n != 0:
                nums[nonZeroIndex] = n
                nonZeroIndex += 1
                
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
