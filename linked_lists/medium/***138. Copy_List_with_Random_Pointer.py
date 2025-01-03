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
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
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

        # Step 1: Clone the nodes and insert them after the original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Set the random pointers for the new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the two lists (original and copied)
        curr = head
        copy_head = head.next
        copy_curr = head.next
        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next         
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head
