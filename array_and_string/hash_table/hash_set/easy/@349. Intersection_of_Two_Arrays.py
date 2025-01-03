# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:15:22 2019

@author: z.chen7
"""

# 349. Intersection of Two Arrays
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
import collections


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1 & set2
        return list(intersection)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums1)

        ans = []
        for num in nums2:
            if counter.get(num, 0) > 0:
                ans.append(num)
                counter[num] = 0

        return ans
