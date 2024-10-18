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
import collections


class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.window = collections.deque()
        self.curr_sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        self.curr_sum += val

        if len(self.window) > self.size:
            self.curr_sum -= self.window.popleft()

        return self.curr_sum / len(self.window)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)