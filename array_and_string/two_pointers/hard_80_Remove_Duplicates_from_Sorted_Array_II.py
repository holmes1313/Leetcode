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
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = right = 0

        while right < len(nums):
            count = 1
            while right+1<len(nums) and nums[right] == nums[right+1]:
                count += 1
                right += 1
            for _ in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            right += 1

        return left