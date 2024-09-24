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
        result = []
        intervals.sort(key=lambda i: i[0])
        for i in intervals:
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        curr_start, curr_end = intervals[0]
        result = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if curr_end >= start:
                curr_end = max(curr_end, end)
            else:
                result.append([curr_start, curr_end])
                curr_start = start
                curr_end = end
        result.append([curr_start, curr_end])
       
        return result

