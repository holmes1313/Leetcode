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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        curr1 = curr2 = head
        while curr1:
            length += 1
            curr1 = curr1.next
        
        if length < n:
            return False
        
        if length == n:
            return head.next
        
        for i in range(length - n - 1):
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return head
            
            