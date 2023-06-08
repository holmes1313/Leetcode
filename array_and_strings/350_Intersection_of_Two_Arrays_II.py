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
from collections import Counter
from typing import List


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    count = Counter(nums1)
    result = []
    
    for n in nums2:
        if count.get(n, -1) > 0:
            count[n] -= 1
            result.append(n)
            
    return result


from collections import Counter


class Solution:
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        for key in counts1:
            if key in counts2:
                key_count = min(counts1[key], counts2[key])
                for i in range(key_count):
                    output.append(key)
        return output

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return output








