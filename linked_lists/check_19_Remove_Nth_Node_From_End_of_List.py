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
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Remove the (L−n+1)(L - n + 1)(L−n+1) th node from the beginning in the list , where LLL is the list length.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list.
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        curr2 = dummy
        for _ in range(length - n):
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return dummy.next
            

# better performance
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
            