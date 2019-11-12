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
        
        intervals.sort(key=lambda x: x[1])
        result = [intervals[0][1]]
        
        for i in intervals[1:]:
            gap = {}
            for idx, r in enumerate(result):
                if i[0] >= r:
                    gap[idx] = i[0] - r
            if not gap:
                result.append(i[1])
            else:
                result[sorted(gap.items(), key=lambda kv: kv[1])[0][0]] = i[1]
            
        print result
        return len(result)
                    
        
        
        
        
        
        