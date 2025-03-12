# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:02:28 2019

@author: z.chen7
"""

# 92. Reverse Linked List II

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        first = dummy

        for _ in range(left - 1):
            first = first.next

        curr = first.next
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first.next.next = curr
        first.next = prev

        return dummy.next
