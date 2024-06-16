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
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        sum_till = 0
        for n in nums:
            sum_till += n
            self.sums.append(sum_till)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]
