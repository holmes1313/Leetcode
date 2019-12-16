# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:14:49 2019

@author: z.chen7
"""

# 238. Product of Array Except Self
"""
Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums) - i -1] = right[len(nums) - i] * nums[len(nums) - i]
            
        return [i*j for i, j in zip(left, right)]
