# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:16:10 2019

@author: z.chen7
"""

# 225. Implement Stack using Queues
"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), 
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack)."""
class MyStack1(object):

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        top_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return top_val
        
    def top(self):
        """
        :rtype: int
        """
        return self.q1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
        

class MyStack(object):

    def __init__(self):
        self.q1 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        for _ in range(len(self.q1) - 1):
            self.q1.append(self.q1.popleft())
        
    def pop(self):
        """
        :rtype: int
        """
        top_val = self.q1.popleft()
        return top_val
        
    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
        
