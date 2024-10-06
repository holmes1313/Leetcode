# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:11:15 2019

@author: z.chen7
"""

# -*- coding: utf-8 -*-

# 155. Min Stack
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2."""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        return self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else False

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1] if self.min else False

