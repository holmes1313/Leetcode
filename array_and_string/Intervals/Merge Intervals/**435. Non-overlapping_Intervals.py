# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:17:39 2019

@author: z.chen7
"""

# 435. Non-overlapping Intervals

"""
Share
Given a collection of intervals, find the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""


"""
Which interval would be the best first (leftmost) interval to keep? 
One that ends first, as it leaves the most room for the rest. So take one with smallest end, 
remove all the bad ones overlapping it, and repeat (taking the one with smallest end of the remaining ones). 
For the overlap test, just keep track of the current end, initialized with negative infinity.
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] >= merged[-1][1]:
                merged.append(interval)
            else:
                if interval[1] < merged[-1][1]:
                    merged.pop()
                    merged.append(interval)

        return len(intervals) - len(merged)
