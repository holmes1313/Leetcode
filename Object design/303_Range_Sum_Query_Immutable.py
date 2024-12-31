# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:49:36 2020

@author: z.chen7
"""

# 303. Range Sum Query - Immutable
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.agg_sums = []
        agg_sum = 0
        for num in nums:
            agg_sum += num
            self.agg_sums.append(agg_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.agg_sums[right]
        else:
            return self.agg_sums[right] - self.agg_sums[left-1]
