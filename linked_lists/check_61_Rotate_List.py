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
from typing import Optional
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
            
        k = k % length
        if k == 0:
            return head
        
        fast = slow = head
        
        for _ in range(k):
            fast = fast.next
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        result = slow.next
        fast.next = head
        slow.next = None
        return result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        curr = dummy
        while curr.next is not None:
            length += 1
            curr = curr.next

        if length <= 1:
            return head

        key = k % length
        if key == 0:
            return head
        slow = fast = dummy
        for _ in range(key):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head