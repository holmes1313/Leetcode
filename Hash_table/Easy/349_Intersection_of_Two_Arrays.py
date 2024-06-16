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

class Solution(object):
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        output = []
        for num in c1.keys():
            if num in c2:
                output.append(num)
        return output
    
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1 & s2)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = {}
        result = []

        for x in nums1:
            seen[x] = 1

        for num in nums2:
            if num in seen and seen[num] == 1:
                result.append(num)
                seen[num] = 0

        return result
