# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:16:52 2019

@author: z.chen7
"""

# 61. Rotate List
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        k %= count

        if k == 0:
            return head

        left = right = head
        for _ in range(k):
            right = right.next

        while right and right.next:
            right = right.next
            left = left.next

        new_head = left.next
        right.next = head
        left.next = None
        
        return new_head


    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        
        k = k % length
        if k == 0:
            return head

        # Make the list circular by connecting the last node to the head
        last.next = head

        # Find the new tail, which is at position (length - k - 1)
        # and the new head, which is at position (length - k)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


        