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
import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        for key, val in counter.items():
            if val == 1:
                return key
    
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = []
        for num in nums:
            if num in d:
                d.remove(num) 
            else:
                d.append(num)
        return d[0]
        
    
    
        