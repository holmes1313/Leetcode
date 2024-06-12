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


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # move pointer backwards through the array, each time writing the smallest value pointed at by p1 or p2.
        i1 = m - 1
        i2 = n - 1
        idx = m + n - 1
        while i1 >= 0 and i2 >= 0:
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n1 > n2:
                nums1[idx] = n1
                i1 -= 1
            else:
                nums1[idx] = n2
                i2 -= 1
            idx -= 1
        while i2 >= 0:
            nums1[i2] = nums2[i2]
            i2 -= 1