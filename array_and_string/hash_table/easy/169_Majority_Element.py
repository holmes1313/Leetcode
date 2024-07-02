# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:59:18 2019

@author: z.chen7
"""

# 169. Majority Element
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums) // 2
        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

            if seen[n] > majority_count:
                    return n

    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collection.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
    
