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
def canAttendMeetings(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        
        for i in range(len(intervals)-1):
            if intervals[i][1] < intervals[i+1][0]:
                return False
        return True






