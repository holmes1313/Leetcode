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


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # return collections.Counter(nums).most_common(1)[0][0]
    return sorted(nums)[len(nums) // 2]        


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        half_num = len(nums) // 2
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > half_num:
                return num

class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = 1
        output = nums[0]

        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
                if seen[n] > freq:
                    output = n
                    freq = seen[n]
            else:
                seen[n] = 1

        return output