# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:40:46 2019

@author: z.chen7
"""

# 19. Remove Nth Node From End of List
"""
Given a linked list, remove the n-th node from the 
end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Two pointers: Move the first pointer n steps ahead. 
        # This ensures that the distance between the first and second pointers is n.
        # dummy head simplifies edge cases, such as when we need to remove the head node.
        dummy = ListNode(0)
        dummy.next = head
        left = right = dummy

        for _ in range(n+1):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next