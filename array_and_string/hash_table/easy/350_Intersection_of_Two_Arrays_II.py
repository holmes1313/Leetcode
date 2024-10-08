# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:46:39 2019

@author: z.chen7
"""

# 350. Intersection of Two Arrays II
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?"""
class Solution(object):
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts1 = collections.Counter(nums1)
        result = []
        for num in nums2:
            if counts1.get(num, -1) > 0:
                result.append(num)
                counts1[num] -= 1

        return result

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = collections.Counter(nums1) & collections.Counter(nums2)
        return intersection.elements()
