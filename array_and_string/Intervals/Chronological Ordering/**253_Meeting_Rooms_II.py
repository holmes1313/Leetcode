# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:43:09 2019

@author: z.chen7
"""

# 253. Meeting Rooms II
"""
Given an array of meeting time intervals consisting of start and end 
times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset 
to default code definition to get new method signature.
"""
class Solution(object):    
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1], -1))

        events.sort(key=lambda x: (x[0], x[1]))

        curr_room = 0
        max_room = 0

        for event in events:
            curr_room += event[1]
            max_room = max(max_room, curr_room)

        return max_room

        
        