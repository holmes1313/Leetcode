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
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = curr = ListNode(-101)
        while head:
            if head.val != curr.val:
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next
        return root.next

    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        left = right = head
        while right:
            if right.val != left.val:
                left.next = right
                left = left.next
            right = right.next
        left.next = None

        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

        
    