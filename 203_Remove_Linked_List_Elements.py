# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:57:57 2019

@author: z.chen7
"""

# 203. Remove Linked List Elements
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5"""

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: Listtype
    """
    
    while head and head.val == val:
        head = head.next
    
    curr = head
    
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
  