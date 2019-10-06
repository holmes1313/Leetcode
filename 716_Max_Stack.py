# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:26:17 2019

@author: z.chen7
"""

# 716. Max Stack
"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

# element (x, current_max)
# interaction between pop and popMax
# reversed(list)

class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        m = max(x, self.stack[-1][-1] if self.stack else x)
        self.stack.append((x, m))
        
    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        
    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][-1]

    def popMax(self):
        """
        :rtype: int
        If you find more than one maximum elements, only remove the top-most one.
        """
        max_value = self.peekMax()
        
        holder = []
        while self.stack[-1][0] != max_value:
            holder.append(self.pop())
            
        self.pop()
        
        for value in reversed(holder):
            self.push(value)
        
        return max_value

stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
stack.stack
stack.top()
stack.popMax()
stack.top()
stack.peekMax()
stack.pop()
stack.stack
stack.top()


stack2 = MaxStack()
stack2.push(5)
stack2.push(1)
stack2.popMax()
stack2.stack
stack2.peekMax()


# heapq for reference
from heapq import *

class MaxStack_2(object):

    def __init__(self):
        self.ls = []        # list (stack)
        self.hp = []        # heap
        self.hpd = set()    # id of items deleted in ls but not hp
        self.lsd = set()    # id of items deleted in hp but not ls
        self.id = 0

    def push(self, x):
        self.ls.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self):
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self):
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self):
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
        return x
