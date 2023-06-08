# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:28:02 2019

@author: z.chen7
"""

# 252. Meeting Rooms
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

    def canAttendMeetings2(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals) - 1):
            for j in range(i+1, len(intervals)):
                if self.is_overlapping(intervals[i], intervals[j]):
                    return False
        return True

    def is_overlapping(self, l1, l2):
        return (l1[0] >= l2[0] and l1[0] < l2[1]) or (l2[0] >= l1[0] and l2[0] < l1[1])






