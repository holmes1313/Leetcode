# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:43:17 2019

@author: z.chen7
"""

# 876. Middle of the Linked List
"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one."""


# Each time, slow go 1 steps while fast go 2 steps.
# When fast arrives at the end, slow will arrive right in the middle.

def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

