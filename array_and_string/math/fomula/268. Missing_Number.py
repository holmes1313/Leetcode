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
from typing import List


class Solution:
    def missingNumber2(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return int(expected_sum - actual_sum)

    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums) # insert each element of nums into a set, allowing us to  query for containment in O(1) time
        for n in range(len(nums) + 1):
            if n not in num_set:
                return n

