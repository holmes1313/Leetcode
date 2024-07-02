# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:42:37 2019

@author: z.chen7
"""

#  697. Degree of an Array
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999."""

import collections

def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_index_mapping = collections.defaultdict(list)
    degree = 0
    results = []
    for i, num in enumerate(nums):
        num_index_mapping[num].append(i)
        degree = max(degree, len(num_index_mapping[num]))
        
    for num, indexs in num_index_mapping.items():
        if len(indexs) == degree:
            results.append(indexs[-1] - indexs[0] + 1)
    return min(results)
   
findShortestSubArray([1, 2, 3])


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_mapping = {}
        max_freq = 0
        for idx, num in enumerate(nums):
            if num in index_mapping:
                index_mapping[num].append(idx)
            else:
                index_mapping[num] = [idx]

            max_freq = max(len(index_mapping[num]), max_freq)

        min_len = len(nums)

        for idexes in index_mapping.values():
            if len(idexes) == max_freq:
                min_len = min(min_len, idexes[-1] - idexes[0] + 1)

        return min_len
