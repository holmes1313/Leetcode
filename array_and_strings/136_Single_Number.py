# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:55:38 2019

@author: z.chen7
"""
# 136. Single Number

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for key, val in seen.items():
            if val == 1:
                return key
