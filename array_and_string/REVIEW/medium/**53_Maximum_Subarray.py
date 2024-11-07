# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:14:19 2019

@author: z.chen7
"""

# 53. Maximum Subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle."""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum  = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum

    

