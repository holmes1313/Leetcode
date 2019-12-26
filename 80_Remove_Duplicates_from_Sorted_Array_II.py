# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:04:52 2019

@author: z.chen7
"""

# 80. Remove Duplicates from Sorted Array II
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums 
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        new_index = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[new_index-1] and nums[i] == nums[new_index-2]:
                continue
                
            nums[new_index] = nums[i]
            new_index += 1
            
        return new_index
        