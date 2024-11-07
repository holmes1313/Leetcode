# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:55:39 2019

@author: z.chen7
"""

# 209. Minimum Size Subarray Sum
"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        curr_sum = 0
        min_len = float("inf")
        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:
                min_len = min(min_len, end-start+1)
                curr_sum -= nums[start]
                start += 1

        return min_len if min_len != float("inf") else 0
