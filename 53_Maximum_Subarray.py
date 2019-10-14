# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:14:19 2019

@author: z.chen7
"""

# 53. Maximum Subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""

# Dynamic Programming

def maxSubArray(nums):
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        max_sum = max(max_sum, nums[i])
    
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)    
    
    

