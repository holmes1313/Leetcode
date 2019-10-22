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
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
    

obj = MovingAverage(3)
obj.next(1)
obj.next(10)
obj.next(3)
obj.next(5)












a = collections.deque( maxlen=2)
a.append(1)
a.append(2)
a.append(3)
a
