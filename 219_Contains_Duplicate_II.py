# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:59:13 2019

@author: z.chen7
"""

# 219. Contains Duplicate II

"""
Given an array of integers and an integer k, find out whether there are two 
distinct indices i and j in the array such that nums[i] = nums[j] and the 
absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, val in enumerate(nums):
            if val in dic and i - dic[val] <= k:
                return True
            dic[val] = i
        return False