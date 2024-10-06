# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:10:07 2019

@author: z.chen7
"""

# 560. Subarray Sum Equals K
"""
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""
# use hashmap to hold cumulative sum

import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = collections.Counter()  # cumulative_sum: freq 
        cumulative_sum = 0
        hashmap[cumulative_sum] += 1
        result = 0
        
        for n in nums:
            cumulative_sum += n
            
            if (cumulative_sum - k) in hashmap:
                result += hashmap[cumulative_sum - k]
                
            hashmap[cumulative_sum] += 1
            
        return result
    