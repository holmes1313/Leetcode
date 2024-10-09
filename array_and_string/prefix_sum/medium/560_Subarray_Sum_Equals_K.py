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
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sums = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_sums:
                count += prefix_sums[prefix_sum - k]

            if prefix_sum not in prefix_sums:
                prefix_sums[prefix_sum] = 1
            else:
                prefix_sums[prefix_sum] += 1

        return count

    