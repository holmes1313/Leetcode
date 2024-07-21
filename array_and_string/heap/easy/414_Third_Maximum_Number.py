# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:17:21 2019

@author: z.chen7
"""

# 414. Third Maximum Number
"""
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum."""


class Solution(object):
    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        kth_max = 1
        prev = nums[0]

        for idx in range(len(nums)):
            if nums[idx] == prev:
                continue

            kth_max += 1
            prev = nums[idx]

            if kth_max == 3:
                return nums[idx]

        return nums[0]

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        min_heap = []
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            heapq.heappush(min_heap, nums[i])

            if len(min_heap) > 3:
                heapq.heappop(min_heap)

            seen.add(nums[i])

        if len(min_heap) == 2:
            heapq.heappop(min_heap)

        return min_heap[0]

