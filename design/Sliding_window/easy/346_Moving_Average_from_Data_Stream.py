# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:08:47 2019

@author: z.chen7
"""
# 346. Moving Average from Data Stream
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3"""


class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = collections.deque()
        self.window_sum = 0        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue) > self.size:
            tail = self.queue.popleft()
        else:
            tail = 0
        self.window_sum = self.window_sum + val - tail
        return self.window_sum / float(len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)