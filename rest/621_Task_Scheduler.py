# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:14:45 2019

@author: z.chen7
"""
# 621. Task Scheduler
"""
Given a char array representing tasks CPU need to do. It contains capital letters 
A to Z where different letters represent different tasks. Tasks could be done 
without original order. Each task could be done in one interval. For each interval, 
CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

# https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        most_common_value = counter.most_common(1)[0][1]
        most_common_count = 0
        for k, v in counter.items():
            if v == most_common_value:
                most_common_count += 1
                
        intervalCount = most_common_value - 1
        intervalLength = n - (most_common_count - 1)
        emptySlots = intervalCount * intervalLength
        availableTasks = len(tasks) - most_common_value * most_common_count
        idles = max(0, emptySlots - availableTasks)
        
        print(most_common_value)
        print(most_common_count)
        print(intervalCount)
        print(intervalLength)
        print(emptySlots)
        print(availableTasks)
        print(idles)
        
        return idles + len(tasks)