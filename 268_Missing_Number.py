# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:08:33 2019

@author: z.chen7
"""

# 268. Missing Number
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum of 0..n minus sum of the given numbers is the missing one.
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)  

