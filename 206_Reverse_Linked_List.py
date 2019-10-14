# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:37:26 2019

@author: z.chen7
"""

# 206. Reverse Linked List
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    https://www.youtube.com/watch?v=XDO6I8jxHtA
    """
    prev = None
    current = head
    
    while head:
        head = current.next
        current.next = prev
        prev = current
        current = head
    
    return prev
    





