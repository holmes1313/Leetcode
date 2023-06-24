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
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = []
        self.total = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val

        if len(self.q) > self.size:
            self.total -= self.q[0]
            self.q = self.q[1:]

        return self.total / len(self.q)


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
