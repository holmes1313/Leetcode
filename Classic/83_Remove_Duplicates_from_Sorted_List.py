# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:16:06 2019

@author: z.chen7
"""

# 83. Remove Duplicates from Sorted List
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3"""

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr = head
    
    while curr:
        while curr.next and (curr.next.val == curr.val):
            curr.next = curr.next.next
        curr.next = curr
        
    return head
        
    