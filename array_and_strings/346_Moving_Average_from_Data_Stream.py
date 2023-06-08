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

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sum += val
        if len(self.nums) > self.size:
            self.sum -= self.nums[0]
            self.nums.popleft()
        return self.sum / len(self.nums)


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
