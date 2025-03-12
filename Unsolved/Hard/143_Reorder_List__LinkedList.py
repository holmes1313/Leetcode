# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:39:46 2019

@author: z.chen7
"""

# 143. Reorder List

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # split to halves
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second halv
        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # combine two parts
        curr = head
        while prev:
            nxt = prev.next
            prev.next = curr.next
            curr.next = prev
            curr = curr.next.next
            prev = nxt
        
                    
        
        