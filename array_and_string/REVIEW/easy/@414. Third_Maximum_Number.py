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
Both numbers with value 2 are both considered as second maximum.
"""
import heapq


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None

        for num in nums:
            if num == first or num == second or num == third:
                continue
            
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        return third if third is not None else first

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        min_heap = []
        for num in nums:
            if num not in seen:
                seen.add(num)

                heapq.heappush(min_heap, num)

                if len(min_heap) > 3:
                    heapq.heappop(min_heap)

        if len(min_heap) == 3:
            return min_heap[0]
        else:
            return max(min_heap)
