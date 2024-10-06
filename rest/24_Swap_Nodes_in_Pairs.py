# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:16:12 2019

@author: z.chen7
"""

# 24. Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curr = head
        second = head.next
        pre = ListNode(0)
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = curr
            pre.next = nxt
            
            pre = nxt.next
            curr = curr.next
            
        return second