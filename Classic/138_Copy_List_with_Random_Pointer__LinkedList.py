# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:50:35 2019

@author: z.chen7
"""

# 138. Copy List with Random Pointer

"""
A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer 
points to, or null if it does not point to any node.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # copy nodes
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, None, None)
            curr.next.next = nxt
            curr = nxt
        
        # copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # separate two parts
        second = curr = head.next
        while curr.next:
            head.next = curr.next
            head = head.next
            curr.next = curr.next.next
            curr = curr.next
        head.next = None
        return second
        
