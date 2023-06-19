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
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:  # 1 -> 2 -> 2 -> 3 -> null  val=2
                curr = curr.next
        
        return dummy.next

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head and head.val == val:
            head = head.next

        curr = head

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
  