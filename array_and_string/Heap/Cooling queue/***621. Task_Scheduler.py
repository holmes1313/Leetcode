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
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Most frequent task drives the number of intervals
        task_count = collections.Counter(tasks)
        max_freq = max(task_count.values())
        max_freq_count = task_count.values().count(max_freq)

        # We need to calculate how many empty slots we will have between the most frequent task's executions
        interval_count = max_freq - 1
        interval_len = n - (max_freq_count - 1)
        empty_slots = interval_count * interval_len
        available_tasks = len(tasks) - max_freq * max_freq_count
        idle_count = max(0, empty_slots - available_tasks)

        return len(tasks) + idle_count

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = collections.Counter(tasks)

        # Create a max heap based on task frequencies (we use negative to simulate max-heap)
        max_heap = []
        for task, freq in task_count.items():
            heapq.heappush(max_heap, (-freq, task))

        time = 0
        # This will store tasks on cooldown
        cooling_queue = collections.deque()
        while max_heap or cooling_queue:
            time += 1

            if max_heap:
                # Pop the most frequent task from the max heap
                count, task = heapq.heappop(max_heap)
                count += 1

                # If there are more instances of the task, put it on cooldown
                if count < 0:
                    cooling_queue.append((task, count, time + n))

            # Check if any task is done with its cooldown period and can be pushed back to the heap
            if cooling_queue and cooling_queue[0][2] <= time:
                task, count, _ = cooling_queue.popleft()
                heapq.heappush(max_heap, (count, task))

        return time
