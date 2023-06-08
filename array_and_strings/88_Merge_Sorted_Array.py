# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:45:51 2019

@author: z.chen7
"""

# 88. Merge Sorted Array
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]"""

"""
note:
Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. 
It can completely change the problem, and make it a lot easier.
"""

from typing import List


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        indexMerged = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[indexMerged] = nums1[index1]
                index1 -= 1
            else:
                nums1[indexMerged] = nums2[index2]
                index2 -= 1
            indexMerged -= 1
        
        while index2 >= 0:
            nums1[indexMerged] = nums2[index2]
            index2 -= 1
            indexMerged -= 1

    def merge_2023(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
        # And move p backwards through the array, each time writing the smallest value pointed at by p1 or p2.
        for i in range(m + n - 1, -1, -1):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] >= nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[i] = nums2[p2]
                    p2 -= 1
            elif p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                break
