# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:16:53 2019

@author: z.chen7
"""

# 86. Partition List

"""
Given a linked list and a value x, partition it such that all nodes less 
than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode(0)
        curr1 = dummy1
        dummy2 = ListNode(0)
        curr2 = dummy2

        curr = head
        while curr:
            if curr.val < x:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
            elif curr.val >= x:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
            curr = curr.next

        curr1.next = dummy2.next

        return dummy1.next


    def partition1(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Create two dummy nodes
        less_head = ListNode(0)  # Dummy head for less list
        greater_head = ListNode(0)  # Dummy head for greater list
        
        less = less_head  # Pointer for the less list
        greater = greater_head  # Pointer for the greater list
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current  # Append to less list
                less = less.next
            else:
                greater.next = current  # Append to greater list
                greater = greater.next
            current = current.next
        
        # Connect the two lists
        greater.next = None  # End the greater list
        less.next = greater_head.next  # Connect less list to greater list
        
        # Return the combined list, starting after the dummy node
        return less_head.next