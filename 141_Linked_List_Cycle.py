# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:31:09 2019

@author: z.chen7
"""

# 141. Linked List Cycle
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which 
represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

 
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node."""

# if the Linked List has a cycle walker and runner will meet at some point

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
        
        if fast.val == slow.val:
            return True
    return False