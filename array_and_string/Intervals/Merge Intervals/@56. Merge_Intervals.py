# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:07:00 2019

@author: z.chen7
"""

# 56. Merge Intervals
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        n = len(intervals)
        for interval in intervals[1:]:
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
