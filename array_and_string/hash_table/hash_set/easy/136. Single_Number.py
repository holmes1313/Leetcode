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
class Solution:
    def singleNumber2(self, nums) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = 1
        for key in seen:
            output = key
        return output

    def singleNumber(self, nums) -> int:
        return sum(set(nums)) * 2 - sum(nums)
    